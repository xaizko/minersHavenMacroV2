from pynput import keyboard
# Comment out the line below if not using a .env file
from dotenv import load_dotenv
import os

# Comment out the line below if not using a .env file
load_dotenv()

# Fill in with x,y coordinates you get from getMousePosition.py
BUTTON_COORDINATES = {
    "REBIRTH": (1164,439),
    "REBIRTH_CONFIRM": (737, 449),
    "SETTINGS_OPEN": (1070, 420),
    "LOAD1": (1211, 326),
    "LOAD2": (1218,484),
    "PROGRESS_POINT": (913, 441)
}

START_KEY = keyboard.KeyCode.from_char('r')
END_KEY = keyboard.KeyCode.from_char('q')

# Step size for mouse movement (higher is faster but less human-like)
STEP_SIZE = 10

# Scanning settings
MONITOR_NUMBER = 1  # Change if you want to capture a different monitor
TARGET_COLOR = (52, 255, 109) # Color to scan for
SCAN_INTERVAL_SECONDS = 1 # Time between each scan
SCAN_TOLERANCE = 100 # Lenency for color matching

# Delay time betwen loading setups
MONEY_DELAY_TIME = 2.5  # Time to wait after loading save before loading second loadout

# Optional Features - Set to false if you don't want to use them
# Be sure to configure properly if you enable them

# Webhook settings
USE_WEBHOOK = True
WEBHOOK_URL = os.getenv("WEBHOOK_URL") # .env file is optional, you can replace with just your webhook url if you want
                                       # This is so I don't have to swap out the webhook url when I make changes to the settings
REGION = {
    "top": 332, # Y coordinate of top left corner
    "left": 577, # X coordinate of top left corner
    "width": 775, # Width of the region
    "height": 295 # Height of the region
}

# Auto Rejoin
USE_AUTO_REJOIN = True
AUTO_REJOIN_CHECK_INTERVAL_SECONDS = 5 * 60 # 20 minutes by default, avoid API rate limit
PLAYER_ID = os.getenv("PLAYER_ID") # .env file is optional, you can replace with just your player ID if you want
                                       # This is so I don't have to swap out the player ID when I make changes to the settings
REJOIN_COORDINATES = {
    "PRIVATE_ISLAND": (1144, 813),
    "SELECT_WORLD": (242, 1019),
    "SELECT_SAVE": (242, 1019),
    "RECENT_ITEMS_SPOT_1": (1071, 437), # Try to position this between the two possible locations, there are two possible locations depending on if u have money to skip
}

# Auto Pulse
USE_AUTO_PULSE = False
PULSE_BUTTON = (55, 801) 
AUTO_PULSE_TIMER = 10 # Time to pulse after loading last loadout in seconds