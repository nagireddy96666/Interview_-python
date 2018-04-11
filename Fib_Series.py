def Fib(n):
    a,b=0,1
    while b<n:
        print b
        a,b=b,a+b
        
n=int(raw_input("Enter Your Number::"))
print Fib(n)
