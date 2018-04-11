entries = ['star', 'astr', 'car', 'rac', 'st']
output = [['star', 'astr'], ['car', 'rac'], ['st']]
'''
# Answer
def group_anagrams(entries):


    return ("2. WIP")

#print(group_anagrams(entries))
'''

l=[]
i=0
for i,j in enumerate(entries):
    l.append(entries[i:2+i])
    i+=2
print l


[l[i:i+2] for i in range(0,len(l),2)]
