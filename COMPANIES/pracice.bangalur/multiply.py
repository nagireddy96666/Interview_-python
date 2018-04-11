Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import operator
>>> a=[1,2,3,4]
>>> b=[2,3,4,5]
>>> list(map(operator.mul,a,b))
[2, 6, 12, 20]
>>> c=[3,4,5]
>>> list(map(operator.mul,a,c))

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(map(operator.mul,a,c))
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> list(map(operator.mul,a,b))
[2, 6, 12, 20]
>>> list(map(operator.add,a,b))
[3, 5, 7, 9]
>>> list(map(operator.sub,a,b))
[-1, -1, -1, -1]
>>> list(map(operator.sub,b,a))
[1, 1, 1, 1]
>>> foo=[1,2,3,4]
>>> bar=[1,2,5,55]
>>> l=map(lambda x,y:x*y,foo,bar)
>>> l
[1, 4, 15, 220]
>>> print a+b
[1, 2, 3, 4, 2, 3, 4, 5]
>>> 
