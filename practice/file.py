#f=open('data.text').read().split('\n')
#print f
#in a filecount=len(open("data.text").readlines())#read the the number of lines
#print count#
for line in open('data.text').xreadlines():
    for word in line.split():
        print word()
