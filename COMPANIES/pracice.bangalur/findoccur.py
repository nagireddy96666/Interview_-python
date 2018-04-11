l=['a','b','c','d','a','e','a','e','s']
count=0
#import pdb;pdb.set_trace()
for i,j in enumerate(l):
    if 'a'==j:
        count+=1
        if count==3:
            print i

#occurrence
def occurrence():
    l=[1,2,3,4,2,3,5,6,1,2,6,7]
    d={}
    for i in l:
        if d.has_key(i):
            pass
        else:
            d[i]=l.count(i)
        return d
resdic=occurrence()
print resdic
    
