def fac(n):
    f=1
    while n>=1:
        f=f*n
        n=n-1
    return f
n=5
print fac(n)




s="Hai this krishna reddy python develpoer"
f=''.join(s[i] for i in range(len(s)-1,-1,-1))
print f




f = open("reddy.txt","w")
f.write("this is \n krishnareddy python develper")
f.close()

f = open("reddy.txt","r")
r = f.read().splitlines()[:2]
print r

a="abcdef"
b="ij"
c=[]
for i,j in enumerate(a):
    c.append((a[i],b[j]))
print c

