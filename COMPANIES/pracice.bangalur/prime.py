
for num in range(10,50):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print '%d equals to %d * %d'%(num,i,j)
            break
        else:
            print num,'is as prime number'
            break
'''
noprimes=[i for i in range(2,8) for i in range(i*2,50,i)]
print noprimes
primes=[x for x in range(2,50) if x not in  noprimes]
print primes

i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not(i%j):
            break
        j=j+1
    if(j>i/j):
        print i,"is prime"
    i=i+1
print "GOOD BYE"
'''
        
