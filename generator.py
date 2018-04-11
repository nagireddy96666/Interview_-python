def genarator(n):
    i = 0
    while i<n:
        yield i
        i += 1
a=genarator(10)
print a
print a.next()

"""
def even():
    for i in range(20):
        if i%2 == 0:
            yield i
s = even()
print s.next()
print s.next()
"""
print a.__doc__
