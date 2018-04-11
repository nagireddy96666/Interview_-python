import re
f=open("text.txt","r")
s=f.read()
word=re.findall(r"\b[aeiou][a-z]{1,}",s)
print word
