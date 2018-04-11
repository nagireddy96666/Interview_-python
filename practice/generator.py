def square(n):
    for i in n:
        yield (i*i)
d=square(range(10))
print d.next()
print d.next()
print d.next()

    
