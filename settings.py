from pynput import keyboard
# Uncomment the line below if using a .env file
# from dotenv import load_dotenv
import os

# Uncomment the line below if using a .env file
# load_dotenv()

# Fill in with x,y coordinates you get from getMousePosition.py
BUTTON_COORDINATES = {
    "REBIRTH": (1429, 441),
    "REBIRTH_CONFIRM": (1146, 441),
    "SETTINGS_OPEN": (1390, 425),
    "LOAD1": (1510, 329),
    "LOAD2": (1540, 481),
    "PROGRESS_POINT": (1231, 441)
}

START_KEY = keyboard.KeyCode.from_char('r')
END_KEY = keyboard.KeyCode.from_char('q')


# Step size for mouse movement (higher is faster but less human-like)
STEP_SIZE = 10

# Scanning settings
MONITOR_NUMBER = 1  # Change if you want to capture a different monitor
TARGET_COLOR = (52, 255, 109)
SCAN_INTERVAL_SECONDS = 1
SCAN_TOLERANCE = 100

# Delay time betwen loading setups
MONEY_DELAY_TIME = 2.5  # Time to wait after loading save before loading second loadout

# Optional Features - Set to true if you want to use them
# Be sure to configure properly if you enable them

# Webhook settings
USE_WEBHOOK = False
WEBHOOK_URL = os.getenv("WEBHOOK_URL") # .env file is optional, you can replace with just your webhook url if you want
                                       # This is so I don't have to swap out the webhook url when I make changes to the settings
REGION = {
    "top": 333, # Y coordinate of top left corner
    "left": 900, # X coordinate of top left corner
    "width": 772, # Width of the region
    "height": 307 # Height of the region
}

# Auto Rejoin
USE_AUTO_REJOIN = False
AUTO_REJOIN_CHECK_INTERVAL_SECONDS = 20 * 60 # 20 minutes by default, avoid API rate limit
PLAYER_ID = os.getenv("PLAYER_ID") # .env file is optional, you can replace with just your player ID if you want
                                       # This is so I don't have to swap out the player ID when I make changes to the settings
REJOIN_COORDINATES = {
    "PRIVATE_ISLAND": (1144, 813),
    "SELECT_WORLD": (771, 1024),
    "SELECT_SAVE": (242, 1019)
}
                                    