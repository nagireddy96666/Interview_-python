import re
list="22 34 l@ak.com r@ed.com hai how are you reee peee deee 12 23 45 987 678."
mat=re.findall('\w+@\w+.\w+',list)
mat1=re.findall('[0-9]{3}',list)
print mat
print mat1
a=iter(mat)
print a
b=iter(mat1)
print b
c=dict(zip(a,b))
print c
