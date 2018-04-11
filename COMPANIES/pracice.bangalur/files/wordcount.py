filename="C:\Users\Brahmaiah\Desktop\pracice.bangalur\files\text.txt"
numlines=0
numwords=0
numchars=0
with open(filename,'r') as file:
    for line in file:
        wordslist=line.split()
        numlines+=1
        numwords+=len(wordslist)
        numchars+=len(line)
#print "lines:%i\n words: %i \n characters: %i",%(numlines,numwords,numchars)
 
