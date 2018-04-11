import numpy as np
a=np.array([1,2,3])
print type(a)
print a.shape
print a[0],a[1],a[2]
a[0]=5
print a
b=np.array([[1,2,3],[4,5,6]])
print b.shape
print b[0,0],b[0,1],b[1,0]
print "array creation"
c=np.zeros((2,2))
print c
d=np.ones((1,2))
print d
e=np.full((2,2),3)
print e
f=np.eye(2)
print f
g=np.eye(4)
print g
h=np.random.random((2,2))
print h
