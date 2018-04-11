f=open("D://an.text","w")
colors = ['red', 'yellow', 'blue']
print f.writelines(colors)
f1=open("D://an.text","r")
data=f1.readlines()
print data
f.close()
