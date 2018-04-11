class vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def squre(self):
        return (self.x**2+self.y**2)
    def add(self):
        return (self.x+self.y)
v=vector(4,5)
print v.squre()
print v.add()
