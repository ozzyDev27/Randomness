import re
with open("essay.txt","r") as f:
    txt=f.read()
rep = {
    "hello": "he loh", 
    "oh": "ow"
    }
rep = dict((re.escape(k), v) for k, v in rep.items()) 
pattern = re.compile("|".join(rep.keys()))
text = pattern.sub(lambda m: rep[re.escape(m.group(0))], txt)
print(text)