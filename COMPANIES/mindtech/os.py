import os
import sys
import re
s="hello this is file hello hello this is python "
x=re.search("hello",s)
print 'x:',x.group()
a=re.findall("hello",s)
b=re.match("ttt",s)
y=b.group()
print "y:",y,"\n",a,"\n","groups:",b

