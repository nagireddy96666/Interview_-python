"""List soring with out sorting builtin methods"""
a = [5, 2, 4, 1,20,41,0,9,13,7]
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

print a



l=[6,34,5,82,54,8,2,1,0,9,4]
print InsertionSort(l)
