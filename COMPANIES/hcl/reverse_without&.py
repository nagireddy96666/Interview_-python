s="ab$def$"
l=[i for i in range(len(s)) if s[i]=='$']
x=list(s.replace('$','')[::-1])
for i in l:
    x.insert(i,'$')
res="".join(x)
print res
