import time

def get_time_angles():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    sec_angle = seconds * 6      # 360 / 60
    min_angle = minutes * 6

    return sec_angle, min_angle