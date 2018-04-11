'''l=[2,1,3,4,59,87,-1,-5,-8]
s=[]
while l:
    minimum=l[0]
    for i in l:
        if i<minimum:
            minimum=i
    s.append(minimum)
    l.remove(minimum)
print s
'''
x=[8,2,4,9,1,4,3]
for i in range(len(x)-1):
    import pdb;pdb.set_trace()
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
    
print x
