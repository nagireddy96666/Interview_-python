#This is based on keys
d={'a':4,'c':2,'e':1,'b':5,'d':3}

for key,value in sorted(d.iteritems(),key=lambda(k,v):(k,v)):
    print "%s:%s"%(key,value)
print ".............."

#this is based on value
for key,value in sorted(d.iteritems(),key=lambda(k,v):(v,k)):
    print "%s:%s"%(key,value)
    

