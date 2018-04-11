t=('name',1,2,3,4,5,3,2,7,'lname')
flag=False
count=0
sum=0
for i,j in enumerate(t):
    if i==1:
        flag=True
    if i==len(t)-1:
        flag=False
    if flag:
        count+=1
        sum+=j
        print j
avg=sum/count
print sum,avg

print reduce(lambda x,y:x+y,t[1:-1])/len(t[1:-1])

