x=open('friends.txt','r')
s=x.read()
x.close()
l=s.split('\n')
#print set([i if  ",".join(i.split(',')[::-1]) not in l else ",".join(sorted(i.split(',')))  for i in l])
print set([",".join(sorted(i.split(','))) for i in l])      




'''y=s.split('\n')
print y
for i in y:
    if 'u1,u2' in y:
        f=open("newfriend2.txt","w")
        f.write("u1,u2")
        f.close()
    elif 'u2,u3' in y:
        f=open("newfriend2.txt","a+")
        f.write("u2,u3")
        f.close()
    elif 'u3,u4' in y:
        f=open("newfriend2.txt","a+")
        f.write("u3,u4")
        f.close()'''





    
    
