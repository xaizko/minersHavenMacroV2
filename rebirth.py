import time
import mouseMovement
from pynput.keyboard import KeyCode, Controller as KeyController
from settings import BUTTON_COORDINATES, MONEY_DELAY_TIME, STEP_SIZE

keyboard = KeyController()

def clickRebirth():
    # Rebirth button placement
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["REBIRTH"])
    time.sleep(0.02)
    mouseMovement.click_left()

def confirmRebirth():
    # Confirm rebirth
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["REBIRTH_CONFIRM"])
    mouseMovement.click_left()
    time.sleep(0.02)

def openLoadout():
    # Open loadout
    keyboard.press(KeyCode.from_char('l'))
    keyboard.release(KeyCode.from_char('l'))

def loadSave1():
    # Load save 1
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["LOAD1"])
    time.sleep(0.8)
    mouseMovement.click_left()
    time.sleep(MONEY_DELAY_TIME)

def loadSave2():
    # Load save 2
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES["LOAD2"])
    time.sleep(0.05)
    mouseMovement.click_left()

def openRebirthMenu():
    # Open rebirth menu
    keyboard.press(KeyCode.from_char('m'))
    keyboard.release(KeyCode.from_char('m'))
    time.sleep(0.1)

def rebirth():
    clickRebirth()
    confirmRebirth()

    openLoadout()
    loadSave1()
    loadSave2()

    openRebirthMenu()