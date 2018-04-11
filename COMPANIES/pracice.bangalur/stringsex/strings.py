s1='abcd'
s2="txyz"
s3='''hi this is brahmi
nice to meet you
bye '''
print "upper==>",s1.upper()
print "title==>",s3.title()
print "capitalize==>",s2.capitalize()
print "find==>",s1.find('meet')
print "replace==>",s3.replace('bye','what are you doing')#It will not effected to the original object
print "find==>",s3.find('bye')
print "s3==>",s3
#"importing string"
import string
sr="hello how are you"
print 'find:',string.find(sr,"hello")
print 'find:',string.find(sr,'hi')
string.find(sr,'how')
#help(str)
#--http://www.python.org/doc/current/lib/string-methods.html
#STRING FORMATTING OPERATOR:"%"
state="california"
print "it never rains in sunny %s."%state
width=24
height=32
depth=8
print 'the box is %d by %d by %d.'%(width,height,depth)
width=24
height='32'
depth='8'
print 'the box is %d by %s by %s.'%(width,height,depth)
l=["hello","how","are","you"]
s=(' ')
x=s.join(l)
print x
#or
y=' '.join(l)
print y

#join examples
>>>",".join(["a","b","c"])




























