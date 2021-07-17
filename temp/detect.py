import cv2
import time
import torch
import logging
import numpy as np

from PyQt5.QtGui import QImage
from PyQt5.QtCore import QSize
from PIL import Image, ImageDraw, ImageFont

from video_stream.video_stream import VideoLoader
from configs.config import *
from model.models import Darknet
from video_stream.visualize import Visualize
from utils.utils import non_max_suppression, load_classes, calc_fps
from model.transform import transform, stack_tensors, preds_postprocess
from handler.intrusion_handling import IntrusionHandling
from handler.alarm import Alarm


def get_model(config_path, img_size, weights_path, device):
    model = Darknet(config_path, img_size=img_size)
    model.load_darknet_weights(weights_path)

    model = model.to(device)
    model.eval()  # Set in evaluation mode
    return model


# model: YOLO模型
# input_tensor: 一个Tensor
# device: cuda0
# num_classes: ？
# conf_thres: 置信度阈值
# nms_thres: ？
def inference(model, input_tensor, device, num_classes, conf_thres, nms_thres):
    try:
        torch.cuda.empty_cache()  # 修复 RuntimeError: cuDNN error: CUDNN_STATUS_EXECUTION_FAILED
        input_tensor = input_tensor.to(device)
        # print(input_tensor.shape)

        output = model(input_tensor)
        preds = non_max_suppression(output, conf_thres, nms_thres)
    except RuntimeError as e:
        torch.cuda.empty_cache()
        preds = [None for _ in range(input_tensor.shape[0])]
        print(e)
        logging.error(e)
    # preds = non_max_suppression(output, num_classes, conf_thres, nms_thres)
    return preds


def array_to_q_image(img, size):
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    if isinstance(size, QSize):
        q_image = q_image.scaled(size)
    else:
        q_image = q_image.scaled(size[0], size[1])
    return q_image


def img_add_title(img, text, left, top, color, size):

    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    font_style = ImageFont.truetype("font/simsun.ttc", size, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, color, font=font_style)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def change_vis_stream(index):
    global vis_name
    global prev_vis_name

    prev_vis_name = vis_name
    vis_name = list(video_stream_paths_dict.keys())[index]


def detect_main(q_thread):
    q_thread.status_update.emit('模型加载')
    device = torch.device(device_name)
    # 获取检测模型
    model = get_model(config_path, img_size, weights_path, device)

    q_thread.status_update.emit('连接OPC服务')
    opc_client = None

    q_thread.status_update.emit('初始化异常处理程序')
    visualize = Visualize(masks_paths_dict)
    handling = IntrusionHandling(masks_paths_dict, opc_client)

    q_thread.status_update.emit('连接报警灯')
    alarm = Alarm(server_name, server_port)

    q_thread.status_update.emit('读取视频流')
    video_loader = VideoLoader(video_stream_paths_dict)
    logging.info('Video streams create: ' + ', '.join(n for n in video_stream_paths_dict.keys()))

    q_thread.status_update.emit('准备就绪')
    classes = load_classes(class_path)

    since = patrol_opc_nodes_clock_start = update_detection_flag_clock_start = time.time()

    accum_time, curr_fps = 0, 0
    show_fps = 'FPS: ??'

    prevs_frames_dict = None
    logging.info('Enter detection main loop process')
    while True:
        curr_time = time.time()

        if curr_time - update_detection_flag_clock_start > update_detection_flag_interval:
            update_detection_flag_clock_start = curr_time
            q_thread.detection_flag.value = 1

        vis_images_dict = video_loader.getitem()
        img_title_dict = station_name_dict.copy()

        active_streams = []
        input_tensor = []
        for name in vis_images_dict.keys():
            if vis_images_dict[name] is None:
                if prevs_frames_dict is not None:
                    vis_images_dict[name] = prevs_frames_dict[name]
                    # 将图片转换成 PyTorch Tensor
                    tensor = transform(vis_images_dict[name], img_size)
                    input_tensor.append(tensor)
            else:
                active_streams.append(station_name_dict[name])
                tensor = transform(vis_images_dict[name], img_size)
                input_tensor.append(tensor)

        if len(input_tensor) == len(vis_images_dict):
            prevs_frames_dict = vis_images_dict
        elif len(input_tensor) == 0:
            print("未读到任何视频帧")
            time.sleep(0.5)
            continue
        # 将多张图片的Tensor堆叠一起，相当于batch size
        input_tensor = stack_tensors(input_tensor)

        # model inference and postprocess
        preds = inference(model, input_tensor, device, 80, conf_thres, nms_thres)
        print(preds)

        if prevs_frames_dict is None:
            not_none_streams = [x for x in vis_images_dict.keys() if vis_images_dict[x] is not None]
        else:
            not_none_streams = list(vis_images_dict.keys())
        # 返回值只有非None视频流的预测结果
        preds_dict = preds_postprocess(preds, not_none_streams, frame_shape, img_size, classes)

        judgements_dict = handling.judge_intrusion(preds_dict)

        since, accum_time, curr_fps, show_fps = calc_fps(since, accum_time, curr_fps, show_fps)

        vis_images_dict = visualize.draw(vis_images_dict, preds_dict, judgements_dict, show_fps)

        handling.handle_judgement(judgements_dict, vis_images_dict, alarm)

        if vis_name in vis_images_dict:
            img = vis_images_dict[vis_name]
            img = img_add_title(img, img_title_dict[vis_name], 10, img.shape[0] - 35, (0, 255, 0), 35)
            qsize = q_thread.main_window.video_display_1.size()
            q_image = array_to_q_image(img, qsize)
            q_thread.video_1_change_pixmap.emit(q_image)

        if prev_vis_name in vis_images_dict:
            prev_img = vis_images_dict[prev_vis_name]
            prev_title = img_title_dict[prev_vis_name]
            vis_images_dict[vis_name] = prev_img
            img_title_dict[vis_name] = prev_title
            vis_images_dict.pop(prev_vis_name)
            img_title_dict.pop(prev_vis_name)

        for title, (i, img) in zip(img_title_dict.values(), enumerate(vis_images_dict.values())):
            img = img_add_title(img, title, 10, img.shape[0] - 35, (0, 255, 0), 35)

            qsize_v = q_thread.main_window.video_display_2.size()
            q_image_v = array_to_q_image(img, qsize_v)

            qsize_h = q_thread.main_window.video_display_5.size()
            q_image_h = array_to_q_image(img, qsize_h)
            if i == 0:
                q_thread.video_2_change_pixmap.emit(q_image_v)
            elif i == 1:
                q_thread.video_3_change_pixmap.emit(q_image_v)
            elif i == 2:
                q_thread.video_4_change_pixmap.emit(q_image_v)
            elif i == 3:
                q_thread.video_5_change_pixmap.emit(q_image_h)
            elif i == 4:
                q_thread.video_6_change_pixmap.emit(q_image_h)
            elif i == 5:
                q_thread.video_7_change_pixmap.emit(q_image_h)
            else:
                raise RuntimeError("No so many QLabel!")
