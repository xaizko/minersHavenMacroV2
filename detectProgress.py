import mss
import numpy as np
from settings import MONITOR_NUMBER

def detect_pixel(point_x, point_y, target_color, tolerance=30):
    with mss.mss() as sct:
        monitor = sct.monitors[MONITOR_NUMBER] 
        img = np.array(sct.grab(monitor))
        pixel_color = img[point_y, point_x][:3]

        distance = np.linalg.norm(pixel_color - target_color)
        return distance <= tolerance