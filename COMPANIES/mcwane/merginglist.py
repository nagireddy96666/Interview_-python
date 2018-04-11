l1=[1,2,3,4,5]
l2=[1,2,10,11]
for i in l2:
    if i not in l1:
        l1.append(i)
print l1
