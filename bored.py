from random import randint as r
while True:
    n=0
    while r(1,8192)!=1:
        n+=1
    print(n)