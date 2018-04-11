"""1. this is using negitive index"""
s="hai this is lakshma reddy"
a=s[::-1]
print a ," 1st"
"""@@@@2nd method"""
l=s.split()
print l
r="\t".join(reversed(l))
print r ,"2nd"
"""@@@3rd method"""
z="".join((s[i] for i in range(len(s)-1,-1,-1)))
print z
"""@@@4th method"""     

def krish(s):
    if len(s) <= 1:
        return s
    return krish(s[1:]) + s[0]
s ="reddy"
print krish(s)
"""@@@5"""
my_string = "Hello World"
for x in range(len(my_string)):
  print my_string[len(my_string)-x-1]
"""@@@6"""  
for x in range(len(my_string), 0, -1):
  print my_string[x-1]

print range(6,0,-1)
"""List leverse """
l=[1,2,3,4,5,6]
l1=[]
for i in range((len(l)-1),-1,-1):
    l1.append(l[i])
print l1
    
