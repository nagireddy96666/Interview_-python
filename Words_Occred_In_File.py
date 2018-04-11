f=open('text2.txt','w')
f.write("hai this is lakshma and this is my first progm \n good morning")
f.close()
d={}
with open ('text2.txt','r') as f:
    lines=f.readlines()
    for line in lines:
        a=line.split()
        print a
        for word in a:
            if word in d:
                d[word]=d[word]+1
            else:
                d[word]=1
print d
    
    
    
