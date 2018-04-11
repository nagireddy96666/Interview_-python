A0=sorted(dict(zip(['a','b','c','d'],[1,2,3,4])))
print "A0:",A0
A1=range(10)
print "A1:",A1
A2=[[i,i*i] for i in A1]
print "A2:",A2
A3={i:i*i for i in A1}
print "A3:",A3
A4=[i for i in A1 if i in A0]
print "A4:",A4
A5=[A0[s] for s in A1 if s in A0]
print "A5:",A5
