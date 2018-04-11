import random
s="hai this is lakshma reddy"
s1=s.split()
print s1

l1=[s1[random.randrange(len(s1))] for i in range(len(s1))]
print l1

