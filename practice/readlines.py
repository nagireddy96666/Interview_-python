name = raw_input("Enter the file name: ")
fobj = open(name)
print fobj.read().split()
for i in enumerate(fobj.read().split()):
    print i
fobj.close()
