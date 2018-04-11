def fun1(med1):
	def fun2():
		results=med1()+2
		return results
	return fun2

@fun1
def fun():
	return 10

fun()

#Every Generator is a iterator
def hello(num):
	for i in range(num):
		yield i
x=hello(10)
x.next()
#reverse of a given data without using built in functions
>>> def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

		
>>> for char in reverse('golf'): 
	print char

	
f
l
o
g
>>> d="hello world"
>>> d.split()
['hello', 'world']
>>> d="g o l f"
>>> d.split()
['g', 'o', 'l', 'f']
>>> data="golf"
>>> x=list(data[i] for i in range(len(data)-1,-1,-1))
>>> print x
['f', 'l', 'o', 'g']
>>> type(x)
<type 'list'>
>>> x="hello"
>>> c=""
>>> cnt=-1
>>> for i in x:
	c+=x[cnt]
	cnt+=-1

	
>>> c
'olleh'
>>> 



