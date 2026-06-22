import mss
import mss.tools
from settings import WEBHOOK_URL, REGION
import requests

region = REGION

def capture_region():
    with mss.mss() as sct: 
        img = sct.grab(region)
        return img

def convert_to_bytes(img):
    return mss.tools.to_png(img.rgb, img.size)

def send_webhook(message, image_bytes: bytes = None):
    payload = {
        "content": message
    }

    files = None
    if image_bytes is not None:
        files = {
            "file": ("screenshot.png", image_bytes, "image/png")
        }

    response = requests.post(WEBHOOK_URL, files=files, data=payload)
    return response