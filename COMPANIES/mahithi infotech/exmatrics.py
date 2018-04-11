a=[[1,3,4],[2,4,7]]
b=[[2,4,6],[7,8,9]]
c=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
for r in c:
    print r
X=[[1,3,4],[2,4,7]]

result = [[X[i][j] for i in range(len(X))] for j in range(len(X[0]))]

for r in result:
   print(r)
