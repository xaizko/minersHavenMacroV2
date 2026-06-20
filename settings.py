from pynput import keyboard

# Fill in with x,y coordinates you get from getMousePosition.py
BUTTON_COORDINATES = {
    "REBIRTH": (1429, 509),
    "REBIRTH_CONFIRM": (1146, 533),
    "SETTINGS_OPEN": (1390, 425),
    "LOAD1": (1510, 329),
    "LOAD2": (1540, 489),
}

START_KEY = keyboard.KeyCode.from_char('r')
END_KEY = keyboard.KeyCode.from_char('q')