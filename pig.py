from random import randint as r
score=0
cpu=0
while score<30 and cpu<30:
    roll=r(1,6)
    cpuroll=r(1,6)
    print(f"You rolled a {roll}!")
    print(f"CPU rolled a {cpuroll}")
    if not roll-1:
        print("Your score has been reset!")
        score=0
    else: score+=roll
    cpu+=cpuroll if cpuroll-1 else -cpu
    print(f"The current score is {score}-{cpu}")
    if input("Continue?\n> ").lower() in ("n","no"):
        print("dumb loser")
        break
while score>=30:print("You win! Finally something good in your life. Good job. You've wasted your time.")
while cpu>=30:print("You lose! Still, everything is lost. You will never win. You've wasted your time.")