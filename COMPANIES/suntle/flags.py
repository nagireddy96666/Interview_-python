a = [2,4,1,1,1,1,11,6]
sum=0
flag=False
for j,i in enumerate(a):
    #print j,
    if j==2:
        flag=True
    if j==len(a)-2:
        flag=False
    if flag:
        #print i
        sum+=i
print sum
        
    
