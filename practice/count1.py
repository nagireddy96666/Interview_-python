l=[1,2,3,5,2,1,3,7,6,5,7,7]
d={ }
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print d        
        
