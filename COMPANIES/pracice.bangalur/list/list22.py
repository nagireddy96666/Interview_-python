l=[]
a=[]
n=int(raw_input("enter the number:"))
for i in range(0,n):
    l.append(i)
    #print l
    for i in l:
        if i not in l:
            a.append(i)
print "l:",l
print "a:",a
    
