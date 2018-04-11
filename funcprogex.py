m = map(lambda x:x*x,range(1,20))
print"map sequence", m
f = filter(lambda x:x%2,range(10))
print "filter sequence", f
r = reduce(lambda x,y:x+y,range(10))
print "reduce value",r
