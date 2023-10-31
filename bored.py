from random import randint as r
n=0
k=0
while n!=1:
    k+=1
    n=0
    while r(1,8192)!=1:
        n+=1
    print(n)
print(k)