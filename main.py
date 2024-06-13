import os
import threading
import time

from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Button, Controller

os.system("stty -echo")  # hide output in unix systems

TOGGLE_KEY = KeyCode(char="k")
QUIT_KEY = KeyCode(char="q")
clicking = False
mouse = Controller()

# Event to signal the thread to stop
stop_event = threading.Event()


def clicker():
    while not stop_event.is_set():
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.5)


def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
    if key == QUIT_KEY:
        clicking = False
        stop_event.set()
        return False  # Stop the listener


if __name__ == "__main__":
    print("Press (k) to toggle clicker and (q) to quit")
    click_thread = threading.Thread(target=clicker)
    click_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

    click_thread.join()  # Wait for the clicker thread to finish
    print("Program terminated.")
