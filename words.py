import re
with open("essay.txt","r") as f:
    txt=f.read()
rep = {
    "hello": "he loh", 
    "oh": "ow"
    }
print(re.compile("|".join(rep.keys())).sub(lambda m: dict((re.escape(k), v) for k, v in rep.items())[re.escape(m.group(0))], txt))
