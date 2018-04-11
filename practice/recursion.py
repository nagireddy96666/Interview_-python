def f(n):
    n=int(input("enter a number"))
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
        return (f(n)*(f(n-1)+f(n-2)))
f(n)
