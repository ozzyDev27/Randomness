from difflib import get_close_matches
from english_words import english_words_set as words
def close(string):
	try:return get_close_matches(string.lower(),words)[0]
	except:return "No match found"
if __name__ == "__main__":while True: print(close(input("> ")))
