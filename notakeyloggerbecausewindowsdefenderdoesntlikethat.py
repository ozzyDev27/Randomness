import pynput
from pynput.keyboard import Key, Listener
  
keys = []
  
def on_press(key):
     
    keys.append(key)
     
    try:
        print(key.char, end='', flush=True)
         
    except AttributeError:
        print(str(key).removeprefix("Key."), end='\n', flush=True)
with Listener(on_press = on_press) as listener:
                     
    listener.join()