'''
def testing():
    print 'before interact'
    a=10
    b=20
    c=a+b
    import code; code.interact(local=locals())
    print 'after interact'

testing()
'''
def odd(a):
    for i in a:
        if i%2!=0:
            yield i
x=range(1,100)
y=odd(x)
print y
'''
#print y.next()
#print y.next()
for i in y:
    print i
def odd(a):
'''
     


