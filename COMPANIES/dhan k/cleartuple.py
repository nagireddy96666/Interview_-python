t=({},{'c':7},{},{},{},{'a':3},{'b':8},{})
y=filter(lambda x: True if x else False,t)
print y
'''
x=0
>>> y=x if x==10 else 20
'''
l=[]
for i in t:
    if i:
        l.append(i)
print l
