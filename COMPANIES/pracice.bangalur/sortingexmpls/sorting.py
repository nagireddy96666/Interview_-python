l=[[1,2,3],[4,5,6],[7,8,9]]
print l.sort(),l
print l.sort(key=lambda x:x[1]),l
print l.sort(key=lambda x:x[1],reverse=True),l
#sorting of list
list=[1,2,3]
print list.sort(),list
print list.sort(reverse=True),list
#sorting the list without using built in functions

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

#reverse of a given string without using built in functions
def rev(text):
    if len(text)<=1:
        return text
    return rev(text[1:])+text[0]
print rev('hello')
#SORTING A STRING
word="hello world"
print ''.join(reversed(word))

