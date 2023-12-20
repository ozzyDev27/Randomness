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
        print("Goodbye!")
        break
while score>=30:print(f"You win! {score}-{cpu}")
while cpu>=30:print(f"You lose! {score}-{cpu}")
