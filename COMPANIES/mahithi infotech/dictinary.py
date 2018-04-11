l1=[1,2,3]
l2=[4,5,6]
d={}
for i in range(len(l1)):
	d[l1[i]]=l2[i]
print d


x=dict([(i,j) for i,j in zip(l1,l2)])
print x
