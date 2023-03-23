k = 1
s = 0
n=0
while not 0:
    s+=(4/k if n%2==0 else 0-(4/k))
    k += 2
    n+=1
    print(s)