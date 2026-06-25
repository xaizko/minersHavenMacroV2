import time
import mouseMovement
from pynput.keyboard import KeyCode, Controller as KeyController
from settings import BUTTON_COORDINATES, LOADOUT_DELAY_TIME, AUTO_PULSE_TIMER, PULSE_BUTTON, USE_AUTO_PULSE, USE_LOAD_2, USE_LOAD_3

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

def loadSave(loadout):
    # Load a specific save
    mouseMovement.move_mouse_in_steps(BUTTON_COORDINATES[loadout])
    time.sleep(0.8) # Safety net, adjust to your preference
    mouseMovement.click_left()
    time.sleep(LOADOUT_DELAY_TIME) # Set time to 0 if you don't want to wait

def openRebirthMenu():
    # Open rebirth menu
    keyboard.press(KeyCode.from_char('m'))
    keyboard.release(KeyCode.from_char('m'))
    time.sleep(0.1)

def autoPulse():
    time.sleep(AUTO_PULSE_TIMER)
    mouseMovement.move_mouse_in_steps(PULSE_BUTTON)
    mouseMovement.click_left()

def rebirth():
    clickRebirth()
    confirmRebirth()

    openLoadout()
    loadSave("LOAD1")

    if USE_LOAD_2:
        loadSave("LOAD2")

    if USE_LOAD_3:
        loadSave("LOAD3")

    if USE_AUTO_PULSE:
        autoPulse()
    openRebirthMenu()