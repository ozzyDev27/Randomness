from random import choice as r
#`1234567890-=~!@#$%^&*()_+[]\{}|'";:,<.>/?qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM
with open(__file__,"r") as f:chars=f.readlines()[1]
with open("text","w") as f:f.write(''.join([r(list(chars)) for i in range(int(input("Length:\n> ")))]))
