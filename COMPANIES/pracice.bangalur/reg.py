import re
line="cats are dogs smarter than dogs"
matchobj=re.match(r'cats',line)#
if matchobj:
    print matchobj.group()
else:
    print "no match"
'''
searchobj=re.search(r'dogs',line)
if searchobj:
    print "seach --> searchobj.group(1):",searchobj.group()
else:
    print "nothing found"
	    
print "#"*40
#this sub method replaces all occurrences of the RE pattern in string with repl,substituting all occurrence unless max provided this method return modified string
phone="2004-959-559 # this is phone number"
num=re.sub(r'phone','mobile',phone)
print num

match ckecks for a match only at the begging of the string,while search checks for a match anywhere in the string 
'''
