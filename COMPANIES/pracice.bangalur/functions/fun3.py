'''
def fun2():
	global b
	print 'b:',b
	b=33
	print 'global:',b
b=100
fun2()
print 'b outside fun2',b
'''
l=[[1,8,3],[4,2,6],[7,5,9]]
n1=[]
while l:
        m=l[0]
        for i in l:
                if i>m:
                        m=i
        n1.append(m)
        l.remove(m)
print n1
