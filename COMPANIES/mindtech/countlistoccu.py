l=[1,2,3,1,2,1,2,1]
l1={}
for i in l:
    if i not in l1:
        l1[i]=1
    else:
        l1[i]+=1
#print l1
for i,j in l1.items():
    print i,":",j
