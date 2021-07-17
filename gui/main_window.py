# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 29pt \"宋体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(35, 35, 40);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(9, 13, 31, 255), stop:1 rgba(23, 26, 43, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setAutoFillBackground(False)
        self.horizontalWidget.setStyleSheet("background-color: rgb(9, 13, 31);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.horizontalWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(44, 48, 58);\n"
"font: 10pt \"宋体\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.video_display_2 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_2.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_2.setText("")
        self.video_display_2.setObjectName("video_display_2")
        self.verticalLayout.addWidget(self.video_display_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.video_display_3 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_3.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_3.setText("")
        self.video_display_3.setObjectName("video_display_3")
        self.verticalLayout.addWidget(self.video_display_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.video_display_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_4.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_4.setText("")
        self.video_display_4.setObjectName("video_display_4")
        self.verticalLayout.addWidget(self.video_display_4)
        self.verticalLayout.setStretch(0, 25)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 25)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 25)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 25)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.video_display_1 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_1.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_1.setText("")
        self.video_display_1.setObjectName("video_display_1")
        self.verticalLayout_4.addWidget(self.video_display_1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.video_display_5 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_5.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_5.setText("")
        self.video_display_5.setObjectName("video_display_5")
        self.horizontalLayout_3.addWidget(self.video_display_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.video_display_6 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_6.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_6.setText("")
        self.video_display_6.setObjectName("video_display_6")
        self.horizontalLayout_3.addWidget(self.video_display_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.video_display_7 = QtWidgets.QLabel(self.horizontalWidget)
        self.video_display_7.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.video_display_7.setText("")
        self.video_display_7.setObjectName("video_display_7")
        self.horizontalLayout_3.addWidget(self.video_display_7)
        self.horizontalLayout_3.setStretch(0, 25)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 25)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 25)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.setStretch(0, 79)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 25)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.setStretch(0, 25)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 75)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_9.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 20pt \"宋体\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalWidget)
        self.textBrowser.setStyleSheet("font: 16pt \"宋体\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(200, 200, 200);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_10.setStyleSheet("color: rgb(85, 255, 255);\n"
"font: 20pt \"宋体\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.record_label = QtWidgets.QLabel(self.horizontalWidget)
        self.record_label.setStyleSheet("background-color: rgb(20, 24, 41);")
        self.record_label.setText("")
        self.record_label.setObjectName("record_label")
        self.verticalLayout_6.addWidget(self.record_label)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 62)
        self.verticalLayout_3.setStretch(2, 8)
        self.verticalLayout_3.setStretch(3, 42)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 72)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 24)
        self.horizontalLayout.setStretch(4, 1)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(9, 13, 31, 255), stop:1 rgba(13, 26, 43, 255));")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(35, 35, 40);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 87)
        self.verticalLayout_2.setStretch(4, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menu_process = QtWidgets.QMenu(self.menubar)
        self.menu_process.setStyleSheet("")
        self.menu_process.setObjectName("menu_process")
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_statistics = QtWidgets.QMenu(self.menubar)
        self.menu_statistics.setObjectName("menu_statistics")
        self.menu_setup = QtWidgets.QMenu(self.menubar)
        self.menu_setup.setObjectName("menu_setup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_run = QtWidgets.QAction(MainWindow)
        self.action_run.setObjectName("action_run")
        self.action_stop = QtWidgets.QAction(MainWindow)
        self.action_stop.setObjectName("action_stop")
        self.action_full_screen = QtWidgets.QAction(MainWindow)
        self.action_full_screen.setObjectName("action_full_screen")
        self.action_exit_full = QtWidgets.QAction(MainWindow)
        self.action_exit_full.setObjectName("action_exit_full")
        self.action_visual = QtWidgets.QAction(MainWindow)
        self.action_visual.setObjectName("action_visual")
        self.action_config = QtWidgets.QAction(MainWindow)
        self.action_config.setObjectName("action_config")
        self.menu_process.addAction(self.action_run)
        self.menu_process.addAction(self.action_stop)
        self.menu_view.addAction(self.action_full_screen)
        self.menu_view.addAction(self.action_exit_full)
        self.menu_statistics.addAction(self.action_visual)
        self.menu_setup.addAction(self.action_config)
        self.menubar.addAction(self.menu_process.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_statistics.menuAction())
        self.menubar.addAction(self.menu_setup.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "西奥电梯智能安全检测系统1区"))
        self.pushButton_6.setText(_translate("MainWindow", "普玛宝轿壁线"))
        self.pushButton_3.setText(_translate("MainWindow", "通用线2-冲"))
        self.pushButton_2.setText(_translate("MainWindow", "萨瓦尼尼2"))
        self.pushButton_4.setText(_translate("MainWindow", "通用线2-折1"))
        self.pushButton_1.setText(_translate("MainWindow", "萨瓦尼尼1"))
        self.pushButton_5.setText(_translate("MainWindow", "通用线2-折2"))
        self.pushButton_7.setText(_translate("MainWindow", "普玛宝激光线"))
        self.label_9.setText(_translate("MainWindow", "实时监测信息"))
        self.label_10.setText(_translate("MainWindow", "异常记录"))
        self.menu_process.setTitle(_translate("MainWindow", "&程序"))
        self.menu_view.setTitle(_translate("MainWindow", "&显示"))
        self.menu_statistics.setTitle(_translate("MainWindow", "&统计"))
        self.menu_setup.setTitle(_translate("MainWindow", "&设置"))
        self.action_run.setText(_translate("MainWindow", "运行"))
        self.action_stop.setText(_translate("MainWindow", "&终止"))
        self.action_full_screen.setText(_translate("MainWindow", "&全屏模式"))
        self.action_exit_full.setText(_translate("MainWindow", "&退出全屏"))
        self.action_visual.setText(_translate("MainWindow", "&异常情况统计与可视化"))
        self.action_config.setText(_translate("MainWindow", "&配置"))