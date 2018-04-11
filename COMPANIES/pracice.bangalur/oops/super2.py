class Testa(object):
    def f1(self):
        print "this is super class Testa"
class Testb():
    def f1(self):
        print "this is sub class in Testb"
class Testc(Testa,Testb):#it will take method from Testb (clas Testc(Testa,Testb)=>it will take method from Testa (MRO))
    def f1(self):
        super(Testc,self).f1()
        print "this is sub class in Testc" 
x=Testc()
x.f1()
