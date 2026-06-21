from pynput import keyboard

# Fill in with x,y coordinates you get from getMousePosition.py
BUTTON_COORDINATES = {
    "REBIRTH": (1429, 441),
    "REBIRTH_CONFIRM": (1146, 441),
    "SETTINGS_OPEN": (1390, 425),
    "LOAD1": (1510, 329),
    "LOAD2": (1540, 481),
    "PROGRESS_POINT": (1231, 443)
}

START_KEY = keyboard.KeyCode.from_char('r')
END_KEY = keyboard.KeyCode.from_char('q')

# Scanning settings
MONITOR_NUMBER = 1  # Change if you want to capture a different monitor
TARGET_COLOR = (52, 255, 109)
SCAN_INTERVAL_SECONDS = 2
SCAN_TOLERANCE = 100

# Delay time betwen loading setups
MONEY_DELAY_TIME = 2  # Time to wait after loading save before loading second loadout

# Webhook settings
WEBHOOK_URL = "WEBHOOK_URL_HERE"
REGION = {
    "top": 0, # Y coordinate of top left corner
    "left": 0, # X coordinate of top left corner
    "width": 1920, # Width of the region
    "height": 1080 # Height of the region
}