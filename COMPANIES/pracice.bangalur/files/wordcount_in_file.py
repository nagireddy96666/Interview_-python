import counter
for line in open(r'C:\Users\Brahmaiah\Desktop\pracice.bangalur\files\text.txt','r'):
    word=counter(line.split())
    print word


from collections import counter
with open("c:python27/python_operators.txt") as f:
    wordcouncounter(f.read().split())
