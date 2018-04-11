s = [-5, -23, 5, 0, 23, -6, 23, 67]
l = []
for i in range(len(s)):
    a = min(s)
    l.append(a)
    s.remove(a)
print l
