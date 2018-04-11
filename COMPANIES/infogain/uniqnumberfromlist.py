l=[1,2,3,1,4,2,5,6,7,8]
#u=set(l)
#print u
l2=[]
l3=[]
for i in l:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
print l2,'\n',l3
