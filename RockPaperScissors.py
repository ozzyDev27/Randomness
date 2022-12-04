import os
def clear():os.system('cls' if os.name=='nt' else 'clear')
def mustInput(s,w):
	n=input(s).upper()
	while not n in w:n=input(s).upper()
	return n
score=[0,0]
match={"RR":0,"RP":2,"RS":1,"PR":1,"PP":0,"PS":2,"SR":2,"SP":1,"SS":0}
repeat=True
while repeat:
	clear()
	players=[]
	for i in range(1,3):players.append(mustInput(f"Use (R) (P) (S)\nPlayer {i}: ",["R","P","S"]));clear()
	if int(match[''.join(players)])!=0:score[int(match[''.join(players)])-1]+=1
	print(f"Player {int(match[''.join(players)])} wins!\nThe score is {score[0]}-{score[1]}" if int(match[''.join(players)])!=0 else f"It's a tie! \nThe score is {score[0]}-{score[1]}")
	repeat=mustInput("Would you like to play again? (Y)/(N)\n> ",["Y","N"])=="Y"
print(f"The score is {score[0]}-{score[1]}!\nThis means it is a tie!" if {score[1]}=={score[0]} else f"The score is {score[0]}-{score[1]}!\nThis means player {int(score[0]<score[1])+1} wins!")
