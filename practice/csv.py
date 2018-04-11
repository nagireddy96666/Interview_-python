import csv
reader = csv.reader(open("C:\Users\Dell\Desktop\practice"))
for title, year, director in reader:
    print year, title
