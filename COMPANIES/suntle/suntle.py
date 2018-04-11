a = [1, 3, 5, 6,20,50,60,80,90,70,30]
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
