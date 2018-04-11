#import pdb;pdb.set_trace()
def f():
    i=0
    if i<=10:
        print i
        i+=1
        f()
    else:
        print "closed"
f()
