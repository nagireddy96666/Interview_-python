def recur_fact(x):
    if x==1:
        return 1
    else:
        return (x*recur_fact(x-1))
num=input("enter a number:")
if num>=1:
    print ("the factorial of",num,"is",recur_fact(num))

    
