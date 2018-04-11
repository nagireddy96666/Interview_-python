s="malayalam"
'''
j=1
for i in len(s):
    if i==s[-j]:
        j=j+1
    else:
        print "given string is palindrome"

x=s[::-1]
print x
print s
'''
s=raw_input("enter the string:")
x=s[::-1]
if x==s:
    print "palindrome"
else:
    print "not palindrome"
    
    
    
