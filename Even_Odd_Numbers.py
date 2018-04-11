l=range(1,15)    
def get_even(l):
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
    return even
def get_odd(l):
    odd=[]
    for i in l:
        if i%2!=0:
            odd.append(i)
    return odd
print get_even(l)
print get_odd(l)
