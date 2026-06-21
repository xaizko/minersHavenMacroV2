import mouseMovement
import os
import requests
import time
from settings import PLAYER_ID, REJOIN_COORDINATES
from rebirth import loadSave1, loadSave2, openLoadout, openRebirthMenu, rebirth

API_URL = "https://presence.roblox.com/v1/presence/users"
IN_GAME_CODE = 2
GAME_ID = 258258996

def getPlayerPresence():
    data = requests.post(
        API_URL,
        json={"userIds": [PLAYER_ID]},
        headers={"accept": "application/json"},
    ).json()
    return data.get("userPresences", [{}])[0].get("userPresenceType", 0)

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
