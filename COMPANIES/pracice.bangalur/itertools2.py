#import itertools
l1=[1,2,3]
l2=[4,5,6]
x=zip(l1,l2)
print x
for i in x:
    print i
for i,j in x:
    print i,j
for i,j in x:
    print i,j,i+j
