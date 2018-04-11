'''
x=raw_input("enter a string:")
count=0
for i in x:
    if i in ("aeiouAEIOU"):
        print i
        count+=1
print count

l=[10,90,70,80,78,98]
a=sorted(l)
print a
b=sorted(a,reverse=True)
print b
i=1
while i<=10:
    print i
    i=i+1

n=input("enter a num:")
i=1
sum=0
while i<=n:
    print i
    sum=sum+i
    i=i+1
print sum

i=1
while i<=5:
    if i==5:
        break
    print i
    i=i+1
'''   
    
a=0
b=1
while b<100:
    print b
    a,b=b,a+b
    

    
