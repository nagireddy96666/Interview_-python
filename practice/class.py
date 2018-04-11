class A():
    def test():
        print "test"
class B():
    def test2():
        print "test2"
class C(A,B):
    def test3():
        print "test3"
c=C()
c.test(100,200)
#print c.test2()
#print c.test3()
