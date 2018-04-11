"""m=map(None,range(1,5),map(lambda x:x*x,range(1,5)),map(lambda x:x*x*x,range(1,5)),map(lambda x:x*x*x*x,range(1,5)))
print m
"""
l=[[1,2],[3,4]]
s=[]
for i in l:
    for j in i:
        s.append(j)
print s

n=map(lambda x:x*x,s)
print n
