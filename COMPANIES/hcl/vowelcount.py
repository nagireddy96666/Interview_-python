l=raw_input("enter a string:")
a=e=i=o=u=0
for j in l:
    if j in "Aa":
        a+=1
    elif j in "Ee":
        e+=1
    elif j in "Ii":
        i+=1
    elif j in "Oo":
        o+=1
    elif j in "Uu":
        u+=1
print "no of a's:",a
print "no of e's:",e
print "no of i's:",i
print "no of o's:",o
print "no of u's:",u
count=a+e+i+o+u
print count
