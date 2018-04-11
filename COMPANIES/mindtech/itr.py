import itertools
t1,t2,t3=[1,123,1]
for i,j,k in itertools.izip_longest(str(t1),str(t2),str(t3),fillvalue=''):
    print i,j,k

