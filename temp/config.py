switch_dict = {
    'salvagnini_1': True,
    'salvagnini_2': True,
    'line_rush': True,
    'line_1': True,
    'line_2': True,
    'prima_power_panel': True,
    'prima_power_laser': True
}

station_name_dict = {
    'salvagnini_1': '萨瓦尼尼1',
    'salvagnini_2': '萨瓦尼尼2',
    'line_rush': '通用线2-冲',
    'line_1': '通用线2-折1',
    'line_2': '通用线2-折2',
    'prima_power_panel': '普玛宝轿壁线',
    'prima_power_laser': '普玛宝激光线'
}

video_stream_paths_dict = {
    'salvagnini_1': 'videos/05.avi',
    'salvagnini_2': 'videos/01.avi',
    'line_rush': 'videos/06.avi',
    'line_1': 'videos/07.avi',
    'line_2': 'videos/04.avi',
    'prima_power_panel': 'videos/02.avi',
    'prima_power_laser': 'videos/03.avi'
}

masks_paths_dict = {
    'salvagnini_1': 'images/masks/salvagnini_1.jpg',
    'salvagnini_2': 'images/masks/salvagnini_2.jpg',
    'line_rush': 'images/masks/line_rush.jpg',
    'line_1': 'images/masks/line_1.jpg',
    'line_2': 'images/masks/line_2.jpg',
    'prima_power_panel': 'images/masks/prima_power_panel.jpg',
    'prima_power_laser': 'images/masks/prima_power_laser.jpg'
}

max_object_bbox_area_dict = {
    'salvagnini_1': 15000,
    'salvagnini_2': 15000,
    'line_rush': 15000,
    'line_1': 15000,
    'line_2': 15000,
    'prima_power_panel': 15000,
    'prima_power_laser': 15000
}

min_object_bbox_area_dict = {
    'salvagnini_1': 500,
    'salvagnini_2': 500,
    'line_rush': 500,
    'line_1': 500,
    'line_2': 500,
    'prima_power_panel': 500,
    'prima_power_laser': 500
}

excluded_objects_dict = {
    'salvagnini_1': [],
    'salvagnini_2': [],
    'line_rush': [],
    'line_1': [],
    'line_2': [],
    'prima_power_panel': [],
    'prima_power_laser': []
}

frame_shape = (480, 640)

vis_name = 'line_2'
prev_vis_name = vis_name

device_name = 'cuda:0'
img_size = 416  # size of each image dimension
config_path = 'configs/yolov3.cfg'  # path to model configs file
weights_path = 'weights/yolov3.weights'  # path to weights file
class_path = 'configs/coco.names'
conf_thres = 0.8  # object confidence threshold
nms_thres = 0.4  # iou threshold for non-maximum suppression

mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = '123456'
mysql_db = 'python_test'

email_opc_warning_interval = 3600

open_mysql_save_record = True

wechat_send_interval = 30

inter_threshold = 0.15

open_opc = False

open_wechat_bot = False

wechat_group = "机器人安全监测"

open_email_report = True

report_statistics_interval = 3600

# 保卫进程读取 detection_flag 值的时间间隔(s) 应大于update_detection_flag_interval
check_detection_process_interval = 65

update_detection_flag_interval = 20

server_name = '192.168.1.6'

server_port = 8080
