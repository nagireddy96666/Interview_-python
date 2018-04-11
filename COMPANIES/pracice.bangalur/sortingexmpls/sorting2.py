data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0] 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print new_list
#------------or2
x=[1,3,5,4,6]
for i in range(len(x)-1):
	if x[i]>x[i+1]:
		x[i],x[i+1]=x[i+1],x[i]

print x
#OR
x=[1,3,5,4,9,8,7,6]
for z in x:
	for i in range(len(x)-1):
		if x[i]>x[i+1]:
			x[i],x[i+1]=x[i+1],x[i]
print x

