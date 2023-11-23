import re
def flatten_list(input_list):
    output_list = []
    for item in input_list:
        if isinstance(item, list):output_list.extend(flatten_list(item))
        else:output_list.append(item)
    return output_list
def format_text(input_filename):
	formatted_content = []
	with open(input_filename, "r") as input_file:content = input_file.read().replace("\n","§").split()
	line = ""
	for word in content:
		if len(line) + len(word) <= 19:line += word + " "
		else:
			formatted_content.append(line.strip())
			line = word + " "
	if line:formatted_content.append(line.strip())
	return flatten_list([i.split("§") for i in formatted_content])
formatted=format_text("input.txt")
import pyautogui
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
def tap(keyTap):
	keyboard.press(keyTap)
	keyboard.release(keyTap)
print(len(formatted))
time.sleep(3)
pageLines=0
#while len(formatted)>0:
#    pageLines+=1
#    if pageLines==15:
#        pyautogui.click(1050, 525)
#        pageLines=0
#    tap(Key.enter)
#    for char in formatted[0]:tap(char)
#    formatted.pop(0)