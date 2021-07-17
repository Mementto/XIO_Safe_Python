import time
import sys
import logging
import os

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPixmap

from gui.main_window import Ui_MainWindow
from detect import detect_main, change_vis_stream

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, detection_flag):
        super().__init__()
        self.detection_flag = detection_flag
        self.setupUi(self)
        self.showFullScreen()
        self.textBrowser.append(time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime()) + '启动检测...')
        self.statusbar.showMessage("系统初始化...")

        th = DetectionThread(self)
        th.video_1_change_pixmap.connect(self.set_frame_1)
        th.video_2_change_pixmap.connect(self.set_frame_2)
        th.video_3_change_pixmap.connect(self.set_frame_3)
        th.video_4_change_pixmap.connect(self.set_frame_4)
        th.video_5_change_pixmap.connect(self.set_frame_5)
        th.video_6_change_pixmap.connect(self.set_frame_6)
        th.video_7_change_pixmap.connect(self.set_frame_7)
        th.text_append.connect(self.append_text)
        th.status_update.connect(self.update_status_message)
        th.start()

        self.pushButton_1.clicked.connect(self.switch_vis_stream_1)
        self.pushButton_2.clicked.connect(self.switch_vis_stream_2)
        self.pushButton_3.clicked.connect(self.switch_vis_stream_3)
        self.pushButton_4.clicked.connect(self.switch_vis_stream_4)
        self.pushButton_5.clicked.connect(self.switch_vis_stream_5)
        self.pushButton_6.clicked.connect(self.switch_vis_stream_6)
        self.pushButton_7.clicked.connect(self.switch_vis_stream_7)
        self.action_stop.triggered.connect(self.process_exit)
        self.action_full_screen.triggered.connect(self.showFullScreen)
        self.action_exit_full.triggered.connect(self.showNormal)

    @pyqtSlot(QImage)
    def set_frame_1(self, image):
        self.video_display_1.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_frame_2(self, image):
        self.video_display_2.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_frame_3(self, image):
        self.video_display_3.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_frame_4(self, image):
        self.video_display_4.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_frame_5(self, image):
        self.video_display_5.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_frame_6(self, image):
        self.video_display_6.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_frame_7(self, image):
        self.video_display_7.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def set_record(self, image):
        self.record_label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(bool)
    def switch_vis_stream_1(self, trigger):
        change_vis_stream(0)

    @pyqtSlot(bool)
    def switch_vis_stream_2(self, trigger):
        change_vis_stream(1)

    @pyqtSlot(bool)
    def switch_vis_stream_3(self, trigger):
        change_vis_stream(2)

    @pyqtSlot(bool)
    def switch_vis_stream_4(self, trigger):
        change_vis_stream(3)

    @pyqtSlot(bool)
    def switch_vis_stream_5(self, trigger):
        change_vis_stream(4)

    @pyqtSlot(bool)
    def switch_vis_stream_6(self, trigger):
        change_vis_stream(5)

    @pyqtSlot(bool)
    def switch_vis_stream_7(self, trigger):
        change_vis_stream(6)

    @pyqtSlot(str)
    def append_text(self, text):
        self.textBrowser.append(text)

    @pyqtSlot(str)
    def update_status_message(self, text):
        self.statusbar.showMessage(text)

    @pyqtSlot(bool)
    def process_exit(self, trigger):
        sys.exit()


class DetectionThread(QThread):
    video_1_change_pixmap = pyqtSignal(QImage)
    video_2_change_pixmap = pyqtSignal(QImage)
    video_3_change_pixmap = pyqtSignal(QImage)
    video_4_change_pixmap = pyqtSignal(QImage)
    video_5_change_pixmap = pyqtSignal(QImage)
    video_6_change_pixmap = pyqtSignal(QImage)
    video_7_change_pixmap = pyqtSignal(QImage)

    record_change_pixmap = pyqtSignal(QImage)

    text_append = pyqtSignal(str)
    status_update = pyqtSignal(str)

    popup_message_box = pyqtSignal(str)

    def __init__(self, main_window):
        super().__init__(main_window)
        self.detection_flag = main_window.detection_flag
        self.main_window = main_window

    def run(self):
        logging.info('开始检测')
        detect_main(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def gui_main(detection_flag):
    sys.excepthook = except_hook  # print the traceback to stdout/stderr

    strftime = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())
    logging.basicConfig(filename='logs/' + strftime + '.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
    logging.info('启动检测程序')

    app = QApplication(sys.argv)
    win = MainWindow(detection_flag)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import multiprocessing

    flag = multiprocessing.Value('i', 0)
    gui_main(flag)
