str="322+455*"
s=str.split("+")
print s
for i in str.split('+'):
    if '*' in i:
        mul=reduce(lambda x,y:x*y,[int(j) for j in i.replace('*','')])
    else:
        total=sum([int(k) for k in i.replace('*','')])
print mul,'\n',total


