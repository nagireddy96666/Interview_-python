l = [1,1,12,3,3,4,3,4,3,4,33,33,44,0]
d = {}
for i in l:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i]=1
print "the list occurence are:",d
