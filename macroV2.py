from timeit import main

from rebirth import rebirth
from pynput import keyboard
from settings import END_KEY, START_KEY

def on_press(key):
    try:
        if key == START_KEY:
            rebirth()

        if key.char == END_KEY:
            return False
    except AttributeError:
        pass

def on_release(key):
    pass

if __name__ == "__main__":
    with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener:
        listener.join()