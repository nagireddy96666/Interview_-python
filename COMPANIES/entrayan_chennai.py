def first_unique(input_string):
    l=[]
    for i in input_string:
        if input_string.count(i)>1:
            continue
        else:
            print i
            break
    return (i)   
input_string = 'treetraversal'
first_unique(input_string)



'''
input_string = 'treetraversal'
for i in input_string:
    if input_string.count(i)>1:
        continue
    else:
        print i
        break
'''
