import time
from ctypes import Structure, byref, c_long, windll
from settings import STEP_SIZE

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

def get_cursor_position():
    point = POINT()
    windll.user32.GetCursorPos(byref(point))
    return point.x, point.y


def send_mouse_input(dx=0, dy=0, flags=0):
    windll.user32.mouse_event(flags, dx, dy, 0, 0)


def move_mouse_in_steps(target_position, steps=STEP_SIZE, step_delay=0.01):
    current_x, current_y = get_cursor_position()
    target_x, target_y = target_position

    for step in range(1, steps + 1):
        progress = step / steps
        next_x = round(current_x + (target_x - current_x) * progress)
        next_y = round(current_y + (target_y - current_y) * progress)

        send_mouse_input(next_x - current_x, next_y - current_y, MOUSEEVENTF_MOVE)
        current_x, current_y = next_x, next_y
        time.sleep(step_delay)

def click_left():
    send_mouse_input(flags=MOUSEEVENTF_LEFTDOWN)
    time.sleep(0.05)
    send_mouse_input(flags=MOUSEEVENTF_LEFTUP)