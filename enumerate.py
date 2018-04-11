l=[12,3,2,4,5,6,10,89,1]
for (i,j) in enumerate(l):
    print i,j
a=[(x,y) for x,y in enumerate(l)]
print a
