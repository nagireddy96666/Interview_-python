'''
class A:
    def __init__(self):
        self.count_def()
        try:
            if sum(self.a)>3:
                raise ValueError
        except ValueError:
            print "obj count not greaterthan 3"
    def count_def(self,a=[]):
        a.append(1)
        self.a=a

            
x=A()
y=A()
z=A()
k=A()
'''
class A:
    def __init__(self):
        self.count_def()
        if sum(self.a)>3:
            raise ValueError
    def count_def(self,a=[]):
        a.append(1)
        self.a=a

            
x=A()
y=A()
z=A()
l=A()

