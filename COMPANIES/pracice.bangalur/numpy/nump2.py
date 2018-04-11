import numpy as np
a=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,1]])
print a[0,1]
print a[0,1]
b=a[:2,1:3]
b[0,0]=77
print a[0,1]
print b
c=a[ :2, 2:4]
print "c is:",c

