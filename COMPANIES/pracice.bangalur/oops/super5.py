class x(object):
    def m1(self):
        print "in m1 of x"
class z():
    def m1(self):
        print "in m1 of z"
class y(x,z):
    def m1(self):
        super(y,self).m1()
        print "in m2 if y"
x1=y()
x1.m1()
'''
output:
in m1 of x
in m2 if y
'''
class x(object):
    def m1(self):
        print "in m1 of x"
class z():
    def m1(self):
        print "in m1 of z"
class y(z,x):
    def m1(self):
        super(y,self).m1()
        print "in m2 if y"
x1=y()
x1.m1()
'''
out put:
in m1 of z
in m2 if y
'''

