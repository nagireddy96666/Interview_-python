s="hello python this is python language"
'''expected out put is
hello:1
python:2
this:1
is:1
language:1
'''
x=s.split()
d={}
for i in x:
    if d.get(i):
        d[i]=d.get(i)+1
    else:
        d[i]=1
print d
