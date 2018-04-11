class Testa(object):
    def f1(self):
        print "this is super class:f1"
class c(Testa):
    def f1(self):
        print "from c"
class Testb(c):
    def f1(self):
        super(c,self).f1()
        super(Testb,self).f1()
        print "this is sub class:f2"
x=Testb()
x.f1()
