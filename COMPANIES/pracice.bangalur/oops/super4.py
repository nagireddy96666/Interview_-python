class A(object):
    def fun1(self):
        print "class A"
class B(A):
    def fun1(self):
        super(B,self).fun1()
        print "class b"

x=B()
x.fun1()
