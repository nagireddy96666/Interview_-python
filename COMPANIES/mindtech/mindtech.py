import itertools
s="this is python"
s1,s2,s3=s.split()
#s1="this"
#s2="is"
#s3="python"
for i,j,k in itertools.izip_longest(s1,s2,s3,fillvalue=' '):
    print i,j,k

print "this is without using fillvalue"
for i,j,k in itertools.izip_longest(s1,s2,s3,fillvalue='0'):
    print i,j,k

