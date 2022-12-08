while 1:from random import randint as r;print(''.join([(char.upper() if r(0,1)==1 else char.lower()) for char in input("> ")]))
