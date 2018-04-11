import math
class Circle():
    def f1(self,r):
        self.r=r
        area=self.r**2*math.pi
        print pi
class Semicircle(Circle):
    def f2(self):
        semiarea=area/2
        print semiarea
z=Semicircle()
z.f2(2)

        
    
