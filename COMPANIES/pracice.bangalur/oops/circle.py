import math
class Circle():
    def __init__(self,r):
        self.r=r
#radius of a circle is 
    def f1(self):
      print self.r**2*math.pi

class Semicircle(Circle):
    def __init__(self,r):
        Circle.__init__(self,r)

    def f2(self):
        print self.r**2*math.pi/2

z=Semicircle(1)
z.f2()
z.f1()