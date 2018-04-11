'''
def generator(seq):
    for i in seq:
        yield i
x=generator([])
print 'dir(generator)',dir(generator),
x=generator([111,222,333])
for i in x:
    print i
x=generator(['aaa','bbb','ccc'])
print x.next()


l=[1,2,3,]
y=iter(l)
print y.next() 
'''

def function(seq):
    for i in seq:
        
l=[1,2,3]
a=function(l)
for i in a:
    print i

