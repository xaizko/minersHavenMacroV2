import mouseMovement
import os
import requests
import time
from webhook import send_webhook
from settings import PLAYER_ID, REJOIN_COORDINATES, USE_WEBHOOK
from rebirth import loadSave1, loadSave2, openLoadout, openRebirthMenu, rebirth

API_URL = "https://presence.roblox.com/v1/presence/users"
IN_GAME_CODE = 2
GAME_ID = 258258996

def getPlayerPresence():
    try:
        data = requests.post(
            API_URL,
            json={"userIds": [PLAYER_ID]},
            headers={"accept": "application/json"},
        ).json()
        return data.get("userPresences", [{}])[0].get("userPresenceType", 0)
    except Exception as e:
        print(f"Error fetching player presence (likely rate limited): {e}")
        if USE_WEBHOOK:
            send_webhook("Error fetching player presence (likely rate limited)")
        return 0

# Returns True if the player is not in the game
def shouldRejoin():
    return getPlayerPresence() != IN_GAME_CODE

def rejoinGame():
    os.startfile(f"roblox://placeId={GAME_ID}")

def selectPrivateIsland():
    mouseMovement.move_mouse_in_steps(REJOIN_COORDINATES["PRIVATE_ISLAND"])
    mouseMovement.click_left()

def selectWorld():
    time.sleep(0.3)                
    mouseMovement.move_mouse_in_steps(REJOIN_COORDINATES["SELECT_WORLD"])
    mouseMovement.click_left()

def selectSave():
    mouseMovement.move_mouse_in_steps(REJOIN_COORDINATES["SELECT_SAVE"])
    mouseMovement.click_left()
    time.sleep(0.2)
    mouseMovement.click_left()

def clickRecentItems():
    mouseMovement.move_mouse_in_steps(REJOIN_COORDINATES["RECENT_ITEMS"])
    time.sleep(0.1)
    mouseMovement.click_left()

def resyncMacro():
    selectPrivateIsland()
    selectWorld()
    time.sleep(30) # Time to join world
    selectSave()
    time.sleep(20) # Time to load save
    
    # In game resync
    openLoadout()
    loadSave1()
    loadSave2()
    openRebirthMenu()
