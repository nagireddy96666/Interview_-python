'''d={'d':3,'b':4,'a':6,'c':2}
k=sorted(d.keys())
print k
s=sorted(d.values())
print s

sorted(d.items(),key=lambda k:k[1])
#[('c', 2), ('d', 3), ('b', 4), ('a', 6)]
sorted(d.items(),key=lambda k:k[0])
#[('a', 6), ('b', 4), ('c', 2), ('d', 3)]
'''
from operator import itemgetter
from collections import OrderedDict

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x1 = OrderedDict(sorted(x.items(), key=itemgetter(0)))#based on keys
sorted_x2 = OrderedDict(sorted(x.items(), key=itemgetter(1)))#based on values
# OrderedDict([(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)])
print sorted_x1,sorted_x2
