l=['a','b','c','d','e','f','a','b','c','d','e','f','a','b','c','d','e','f']
d={}
#expected output=>d={'a':[6,12],'b':[7,13],'c':[8,14],'d':[9,15],'e':[10,16],'f':[11,17]}
'''
for i,j in enumerate(l):
	if j not in d:
		d[j]=[]
	else:
		d[j].append(i)
print d
'''
for i in range(len(l)):
        if l[i] not in d:
                d[l[i]]=[i]
        else:
                d[l[i]]+=[i]
print d
    
