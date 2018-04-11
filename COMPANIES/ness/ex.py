>>> x=(1,2,(4,5,6,7,8))
>>> x[2][1:4]
(5, 6, 7)
>>> "".join([str(i) for i in x[2][1:4]])
'567'
>>> s="apple banna and apple banna "
>>> s.count('apple')
2
>>> s.count('banna')==s.count('apple')
True
>>> l=['apple',['banna','apple']]
>>> l.count('apple')
1
>>> set(l)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(l)
TypeError: unhashable type: 'list'
>>> i='apple'
>>> list(l)
['apple', ['banna', 'apple']]
>>> for i in l:
	if i=="apple:"
	
SyntaxError: invalid syntax
>>> for i in l:
	if i=="apple":
		count+=1
	else:
		x=i.count('apple')
		count+=x

		

Traceback (most recent call last):
  File "<pyshell#18>", line 3, in <module>
    count+=1
NameError: name 'count' is not defined
>>> count=0
>>> for i in l:
	if i=="apple":
		count+=1
	else:
		x=i.count('apple')
		count+=x

		
>>> print count
2
>>> count=0
>>> for i in l:
	if i.count('apple'):
		count+=i.count('apple')
print count
SyntaxError: invalid syntax
>>> 
>>> for i in l:
	if i.count('apple'):
		count+=i.count('apple')
print count
SyntaxError: invalid syntax
>>> for i in l:
	if i.count('apple'):
		count+=i.count('apple')

>>> 
>>> count
2
>>> l=['apple','banaba',['apple','banan']]
>>> count=0
>>> for i in l:
	if i.count('apple'):
		count+=i.count('apple')

		
>>> count
2
>>> l=['banaba',['apple','banan']]
>>> count=0
>>> for i in l:
	if i.count('apple'):
		count+=i.count('apple')

		
>>> count
1
>>> 
