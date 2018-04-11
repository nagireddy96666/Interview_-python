a = input('Enter a number:: ')
def prime(a):
    if a <= 1:
        print a, 'is a not prime'        
    else :
        for i in range (2, a ):
            if a%i == 0:
                print a,' is not a prime number'
                break
        else:
            print "prime number"
    
prime(a)                


