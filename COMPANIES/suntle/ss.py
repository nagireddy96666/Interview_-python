a = [ 1, 5, 4, 2, 8,89, 3, 10, 6]
skip_now = False
sum = 0
for i in a:
    #import pdb;pdb.set_trace()
    if i == 2:
        skip_now = True
        print "true",i
    elif i == 3:
        skip_now = False
        print "false",i
        continue
    if not skip_now:
        print "adding",i
        sum += i
print sum

    
a = [5, 8, 3, 7, 10, 8, 9, 1, 56, 2]

# 3 + 7 + 10 + 9
sum=0
start_adding = False
for i in a:
  if i==3:
    start_adding = True     
  if i == 9:
    sum+=i
    start_adding = False
  if start_adding:
    sum+=i
     
print sum


a = [2.5, 3, 5, 6]
b = [2, 3, 7, 8, 10, 20, 30]
c = []
#c = 1, 2, 3, 3, 5, 6, 7, 8
#min=c[0]

aindex = 0
bindex = 0

while aindex < len(a) and bindex < len(b):
  if a[aindex] < b[bindex]:
    c.append(a[aindex])
    aindex+=1
  else:
    c.append(b[bindex])
    bindex+=1
c.extend(b[bindex:])
print c
'''
for i in range(len(a)):
  if a[i]>b[i]:
    c.append(a[i])
#    else:
 #     c.append()
print c
'''
