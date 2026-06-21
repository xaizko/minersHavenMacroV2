from pynput import keyboard

# Fill in with x,y coordinates you get from getMousePosition.py
BUTTON_COORDINATES = {
    "REBIRTH": (1164,439),
    "REBIRTH_CONFIRM": (737, 449),
    "LOAD1": (1211, 326),
    "LOAD2": (1218,484),
    "PROGRESS_POINT": (913, 441)
}

START_KEY = keyboard.KeyCode.from_char('r')
END_KEY = keyboard.KeyCode.from_char('q')

# Scanning settings
MONITOR_NUMBER = 1  # Change if you want to capture a different monitor
TARGET_COLOR = (52, 255, 109)
SCAN_INTERVAL_SECONDS = 1
SCAN_TOLERANCE = 100

# Delay time betwen loading setups
MONEY_DELAY_TIME = 2  # Time to wait after loading save before loading second loadout

# Webhook settings
WEBHOOK_URL = "WEBHOOK_URL_HERE"  # Replace with your actual webhook URL
REGION = {
    "top": 332, # Y coordinate of top left corner
    "left": 577, # X coordinate of top left corner
    "width": 775, # Width of the region
    "height": 295 # Height of the region
}