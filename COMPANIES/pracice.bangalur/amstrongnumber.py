num=input("enter the number:")
sum=0
temp=num
order=len(str(num))
#while temp>0:
for i in range(order):
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print num,"is an amstrong number:"
else:
    print num,"is not amstrong number"

    
