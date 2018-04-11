def odd(a):
    for i in a:
        if i%2!=0:
            yield i
x=range(1,100)
y=odd(x)

#print y.next()
#print y.next()
for i in y:
    print i
