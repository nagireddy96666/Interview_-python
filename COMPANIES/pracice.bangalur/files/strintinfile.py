import re
f=open("text.txt",'r')
x=f.read()#the total file will come to x,now x is having total file
print "file is:\n",x,"\n number of characters in the file:",len(x)
lines=x.split("\n")#It is going to split as per the lines
print "total lines in the file is",len(lines)
words=x.split()
print "the total words in the file is:",len(words)
y=re.findall(r"\bhi\b",x)#It is going to come in the list,all the occurrence 
print y,"\n","the number of times word will be repeated in the file:",len(y)
string=re.match("hi",x)
print "match:",string
string1=re.match("python",x)
print "match objec:",string1
string2=re.search("python",x)
print "serch:",string2


