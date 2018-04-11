Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
>>> import itertools
>>> itertools.i

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    itertools.i
AttributeError: 'module' object has no attribute 'i'
>>> itertools.izip_longest
<type 'itertools.izip_longest'>
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
this is python
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
t i p
h s y
i   t
s   h
    o
    n
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
t i p
h s y
i   t
    h
    o
    n
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
t i p
h s y
i   t
    h
    o
    n
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
t i p h
h s y e
i   t l
    h l
    o o
    n  
>>> l1=[1,2,3]
>>> l2=[4,5,6]
>>> x=zip(l1,l2)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x=zip(l1.l2)
AttributeError: 'list' object has no attribute 'l2'
>>> x=zip(l1,l2)
>>> x
[(1, 4), (2, 5), (3, 6)]
>>> for i in x:
	print i

	
(1, 4)
(2, 5)
(3, 6)
>>> for i,j in x:
	print i,j

	
1 4
2 5
3 6
>>> for i,j in x:
	print i,j,i+j

	
1 4 5
2 5 7
3 6 9
>>> l
' '
>>> l1
[1, 2, 3]
>>> l2
[4, 5, 6]
>>> l2.append(7)
>>> x=zip(l1,l2)
>>> for i,j in x:
	print i,j,i+j

	
1 4 5
2 5 7
3 6 9
>>> 
============== RESTART: C:/Users/Brahmaiah/Desktop/mindtech.py ==============
t i p h
h s y e
i 0 t l
s 0 h l
0 0 o o
0 0 n 0

