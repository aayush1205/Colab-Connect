import time
import os
import random
if not 'DISPLAY' in os.environ:
    os.environ["DISPLAY"] = ":0"


from pynput.keyboard import Controller, Key

# keyboard = Controller()
# keyboard.press(Key.ctrl)
# keyboard.press(Key.shift)
# keyboard.press(Key.f8)
# keyboard.release(Key.ctrl)
# keyboard.release(Key.shift)
# keyboard.release(Key.f8)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)


def open_serv():
    

    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.f8)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release(Key.f8)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.release(Key.enter)


