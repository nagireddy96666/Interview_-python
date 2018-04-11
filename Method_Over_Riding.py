class A(object):
    def add(self,x,y):
        return x-y
class B(A):
    def add(self,x,y):
        print super(B,self).add(10,20)
        return x+y
b=B()
print b.add(2,4)
