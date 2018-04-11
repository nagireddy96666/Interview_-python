'''def f1(x) :
    print "The values in the given list : ",x,id(x)
    print "Total no of elemnts is : ",len(x)

    x[1]=2000
    x[2]=3000
    x.append(4000)
    
    x=['a','b','c'] # local
    print "in f1,x=",x,id(x)
    l2=['a','b','c'] #local to f1
    print "inside f1, l2=",l2


l1=[10,20,30] #global l1
f1(l1)
print  'outside functin , l1=',l1,id(l1)
#print "outside f1, l2=",l2
'''
def f(a,b,c):
    print a,b,c
l={'a':10,'b':20,'c':30}
f(**l)
print l,id(l)

