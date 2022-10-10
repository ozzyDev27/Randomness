from pynput.keyboard import Key, Controller
from time import sleep as wait
keyboard = Controller()

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def tap(keyTap):
    keyboard.press(keyTap)
    keyboard.release(keyTap)

wait(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
for letter in letters:
    tap(letter)
    
    
#https://typethealphabet.app/
#I used this website!
