import re
mail= '''venkt@gmail.com brahmi@yahoo.com chinna@
gmail.com lachireddy@gmail.com hello@hotmail.com'''
x=re.findall(r"[a-z][a-z0-9_.]{2,}@\n*gmail.com",mail)
print x
s=[]
for i in x:
    s.append(i.split('@')[0])
print s
