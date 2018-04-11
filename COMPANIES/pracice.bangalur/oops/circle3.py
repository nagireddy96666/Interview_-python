#import math
class Circle(object):
    def f1(self,r):
        self.r=r
        self.area=3.14*r**2
        #print self.area
        return self.area
class Semi(Circle):
    def f1(self,r):
        res=super(Semi,self).f1(r)
        #y=x/2

        print res
        print res/2
x=Semi()
x.f1(2)
