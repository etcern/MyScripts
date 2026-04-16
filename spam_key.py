from pynput.keyboard import Key, Controller, Listener 
import time
import threading

# pyinput is a library that allows you to control and monitor input devices. 
# In this case, we are using it to control the keyboard. It runs on the same lever as the 
# Windows API, so it can be used to simulate key presses and releases reliably. 
# Good for game scripting macros :) pyautogui is trash lol

#Git commit 1 test

keyboard = Controller()
time.sleep(3)

# Define gloval alive variable to control macro thread
alive = False

def pressKey():
    while True:
        if alive:
            keyboard.press(Key.shift)
            time.sleep(0.05)
            keyboard.release(Key.shift)
            time.sleep(0.05)
        else:
            time.sleep(0.1)

def on_press(key):
    global alive

    # Toggle with key  (F8 in this case to start/stop the macro)
    if key == Key.f8:
        alive = not alive


# Threading that make sma programmo run in backgrou8ndo  :D daemon is like a background thread that will 
# automatically close when the main program exits. It s normal, since programms use this all 
# the time to run background tasks without blocking the main thread. Once the programm 
# stopps, the daemon thread will also stop, so you dont have to worry about it running forever.
macro_thread = threading.Thread(target = pressKey, daemon=True)
macro_thread.start()


# Listener is a class from the pynput library that allows you to listen for keyboard events before the thread function is executed.
with Listener(on_press=on_press) as listener:
    listener.join()