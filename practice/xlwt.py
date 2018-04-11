import csv
f=open("anreddy.csv")
d=csv.reader(f)
l=[]
for row in d:
    l.append(row[2])
    print l
