'''
primes=[x for x in range(2,200) if all(x % y != 0 for y in range(2, x))]
print primes


#noprimes=[i for i in range(2,14) for i in range(i*2,200,i)]
#primes=[j for j in range(2,200) if j not in noprimes]
l=[]
for i in range(2,200):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
print l
'''
n=input("enter the number:")
for i in range(2,n):
    if n%i==0:
        print "given number is not prime number:"
        break
else:
    print "given number is prime number:"

 
