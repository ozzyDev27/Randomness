from english_dictionary.scripts.read_pickle import get_dict
from pynput.keyboard import Key, Listener, Controller
dictionary = [word.lower() for word in get_dict().keys() if word]
subLetters=input("Gray Letters:\n> ")
mainLetter=input("Main Letter:\n> ")
words=[j for j in [word for word in dictionary if mainLetter in word] if [i for i in j if i in subLetters or i in mainLetter]==[i for i in j] and len(j)>3]
print(words)
keyboard = Controller()
def on_press(key):
    try:
        if key.char == '`':
            for word in words:
                for letter in word:
                    keyboard.tap(letter)
                keyboard.tap(Key.enter)
    except AttributeError:
        pass
with Listener(on_press=on_press) as listener:
    listener.join()
