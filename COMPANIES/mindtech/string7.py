s="hello python this is python language"
x=s.split()
'''
d={}
for i in x:
    if d.get(i):
        d[i]=d.get(i)+1
    else:
        d[i]=1
print d
for i,j in d.items():
    print i,":",j
'''
#or
d={}
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print d
for i,j in d.items():
    print i,":",j
