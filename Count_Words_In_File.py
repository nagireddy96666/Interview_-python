#f=open("text1.txt",'a')
#f.write("Number\tName\tPhNum \n 001\tLakshma\t123456789\n002\tReddy\t234567890")
#f.close
NW=0
with open("text1.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        a=line.split("\t")
        NW += len(a)
print NW        
        

