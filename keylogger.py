# ---------------------------- Imports + pip Setup --------------------------- #
import os
try: import pynput
except: os.system("pip install pynput")
import pynput
from pynput.keyboard import Key,Listener

# --------------------------------- Functions -------------------------------- #
keysPressed=[]
def on_press(key):
    keysPressed.append(key)
    os.clear()
    print(''.join(keysPressed))

# ------------------------------- The Listener ------------------------------- #