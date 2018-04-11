def occurrence():
    #  import pdb;pdb.set_trace()
    l=[1,2,3,4,2,3,5,6,1,2,6,7]
    d={}
    for i in l:
        if d.has_key(i):
            pass
        else:
            d[i]=l.count(i)
            #return d
    return d
resdic=occurrence()
print resdic
