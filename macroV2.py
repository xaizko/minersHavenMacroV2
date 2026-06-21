import threading
import time
import webhook

from detectProgress import detect_pixel
from rebirth import rebirth
from pynput import keyboard
from settings import END_KEY, BUTTON_COORDINATES, START_KEY, TARGET_COLOR, SCAN_INTERVAL_SECONDS, SCAN_TOLERANCE, USE_WEBHOOK

is_scanning = False
scanning = False

def scan_loop():
    global scanning
    while True:
        if is_scanning:
            point_x, point_y = BUTTON_COORDINATES["PROGRESS_POINT"]
            if detect_pixel(point_x, point_y, TARGET_COLOR, tolerance=SCAN_TOLERANCE) and not scanning:
                scanning = True
                print("Progress color detected. Running rebirth...")
                rebirth()
                if USE_WEBHOOK:
                    try:
                        webhook.send_webhook("Rebirth completed successfully.", webhook.convert_to_bytes(webhook.capture_region()))
                    except Exception as e:
                        print(f"Error sending webhook (Check your URL): {e}")
                scanning = False

        time.sleep(SCAN_INTERVAL_SECONDS)

def on_press(key):
    global is_scanning

    try:
        if key == START_KEY:
            if not is_scanning:
                is_scanning = True
                scanning = False
                print("Scanner started.")

        if key == END_KEY:
            if is_scanning:
                is_scanning = False
                print("Scanner paused.")
    except AttributeError:
        pass

def on_release(key):
    pass

if __name__ == "__main__":
    threading.Thread(target=scan_loop, daemon=True).start()

    with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener:
        listener.join()