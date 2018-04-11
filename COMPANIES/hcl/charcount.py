s="hello"
a=lambda i:s.count(i)
x=dict([(i,a(i)) for i in s])
print x
