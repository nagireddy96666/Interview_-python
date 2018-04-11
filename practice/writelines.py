file = open('newfile.txt', 'a')
l=["BTECH\n"," NAGIREDDY\n"," ANNAPUREDDY\n"]
print l
file.write(l)
file = open('newfile.txt', 'r')
print file.readl()
#print file.read()
file.close()            
        

