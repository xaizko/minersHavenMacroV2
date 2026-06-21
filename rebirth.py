import time
import mouseMovement
from pynput.keyboard import KeyCode, Controller as KeyController
from settings import BUTTON_COORDINATES, MONEY_DELAY_TIME, STEP_SIZE

keyboard = KeyController()

def rebirth():
    # Rebirth button placement
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["REBIRTH"])
    time.sleep(0.02)
    mouseMovement.click_left()
    
    # Confirm rebirth
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["REBIRTH_CONFIRM"])
    mouseMovement.click_left()
    time.sleep(0.02)

    # Open settings
    keyboard.press(KeyCode.from_char('l'))
    keyboard.release(KeyCode.from_char('l'))

    # Load save 1
    time.sleep(0.3)
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["LOAD1"])
    mouseMovement.click_left()
    time.sleep(MONEY_DELAY_TIME)

    # Load save 2
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["LOAD2"])
    mouseMovement.click_left()

    # Open rebirth menu
    keyboard.press(KeyCode.from_char('m'))
    keyboard.release(KeyCode.from_char('m'))
    time.sleep(0.1)