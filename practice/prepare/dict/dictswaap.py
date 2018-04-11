def swap(d):
    k = d.keys()
    v = d.values()
    z = zip(v,k)
    print dict(z)
    z1 = zip(k,v)
    print dict(z1)
d = input("enter the dict values:")
swap(d)
