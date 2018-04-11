'''f = open('add.txt', "r")
r = f.read().splitlines()[:2]
print r


s="venkatreddy i am reddy "
z=''.join(s[i] for i in range(len(s)-1,-1,-1))
print z



def val(s):
    if len(s)<=1:
        return s
    return val(s[1:]) + s[0]
s='krishna'
print val(s)

def fact(n):
    f=1
    while n>=1:
        f=f*n
        n=n-1
    return f
n=7
print fact(n)

def fib(n):
    a,b=0,1
    while b<n:
        print b
        a,b=b,a+b
n=12
print fib(n)

def palin(a):
    b=a[::-1]
    if a == b:
        return "paln"
    else:
        return "not"
a=input("enter the string::")
print palin(a)


f=open('trash.txt','w')
f.write("venkat reddy \n redy venkat \n venkat")
f.close()
count=0
f=open('trash.txt','r')
lines=f.readlines()
for line in lines:
    if "v" in line:
        count=count+1
print count
f.close()


d={}
f=open('trash.txt')
lines=f.readlines()
for line in lines:
    a=line.split()
    print a
    for word in a:
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
print d
f.close()

f=open('trash.txt')
f1=open('out.txt','w')
lines=f.readlines()
for line in lines:
    if "venkat" in line:
        f1.write(line)
f.close()

c=[]
l=[1,2,7,2,8,2,82,4,7]
for i in l:
    if i not in c:
        c.append(i)
print c
'''

'''a="abcdef"
b="ijklmn"
c=[]
for i,j in enumerate(a):
    c.append((a[i],b[i]))
print c'''


#l=['red','green','red','blue','block']
cnt = counter()
for word in ['red','biue','red','block']:
    cnt[word] += 1
print cnt    

        

        
        
        


        
