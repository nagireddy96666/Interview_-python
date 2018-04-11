class A:
    cnt=0
    def __init__(self):
        A.cnt+=1
        print A.cnt
        if A.cnt>3:
            raise ValueError

x1=A()
x2=A()
x3=A()
x4=A()
x5=A()
#print "can't create the morethan three objects"
#print A.cnt
