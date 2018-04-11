Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class A:
    a=[]
    def __init__(self):
        a.append(self)

>>> x=A()

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x=A()
  File "<pyshell#1>", line 4, in __init__
    a.append(self)
NameError: global name 'a' is not defined
>>> class A:
    global l=[]
    def __init__(self):
        l.append(self)
        
SyntaxError: invalid syntax
>>> 
>>> class A:
    global l=[]
    def __init__(self):
        l.append(self)
        
SyntaxError: invalid syntax
>>> class A:
	l=[]
	def __init__(self):
		l.append(self)

		
>>> x=A()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x=A()
  File "<pyshell#8>", line 4, in __init__
    l.append(self)
NameError: global name 'l' is not defined
>>> class A:
	l=[]
	def __init__(self):
		global l
		l.append(self)

		
>>> x=A()

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x=A()
  File "<pyshell#11>", line 5, in __init__
    l.append(self)
NameError: global name 'l' is not defined
>>> class A:
	def __init__(self):
		count_def()
	def count_def(self,a=[]):
		a.append(self)
		self.a=a

		
>>> x=A()

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x=A()
  File "<pyshell#17>", line 3, in __init__
    count_def()
NameError: global name 'count_def' is not defined
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(self)
		self.a=a

		
>>> x=A()
>>> y=A()
>>> x.a
[<__main__.A instance at 0x02BB4440>, <__main__.A instance at 0x02BB4CD8>]
>>> x
<__main__.A instance at 0x02BB4440>
>>> x.a
[<__main__.A instance at 0x02BB4440>, <__main__.A instance at 0x02BB4CD8>]
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(self)
		self.a=a
		print sel.a.count()

		
>>> y=A()

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    y=A()
  File "<pyshell#28>", line 3, in __init__
    self.count_def()
  File "<pyshell#28>", line 7, in count_def
    print sel.a.count()
NameError: global name 'sel' is not defined
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(self)
		self.a=a
		print self.a.count()

		
>>> x=A()

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x=A()
  File "<pyshell#31>", line 3, in __init__
    self.count_def()
  File "<pyshell#31>", line 7, in count_def
    print self.a.count()
TypeError: count() takes exactly one argument (0 given)
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(self)
		self.a=a

		
>>> x=A()
>>> x.a
[<__main__.A instance at 0x02BB4FA8>]
>>> y=A()
>>> y.a
[<__main__.A instance at 0x02BB4FA8>, <__main__.A instance at 0x02B825D0>]
>>> c=A()
>>> c.a
[<__main__.A instance at 0x02BB4FA8>, <__main__.A instance at 0x02B825D0>, <__main__.A instance at 0x02BB4508>]
>>> c.a.count()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c.a.count()
TypeError: count() takes exactly one argument (0 given)
>>> c.a.count(self)

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.a.count(self)
NameError: name 'self' is not defined
>>> type(c.a)
<type 'list'>
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(1)
		self.a=a

		
>>> x=A()
>>> x.a
[1]
>>> y=A()
>>> y.
SyntaxError: invalid syntax
>>> y.a
[1, 1]
>>> sum(y.a)
2
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(1)
		self.a=a
		try:
			if sum(self.a)==3:
				raise ValueError
		except ValueError:
			print "obj greaterthan not 3"

			
>>> x=A()
>>> x.a
[1]
>>> y=A()
>>> z=C()

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    z=C()
NameError: name 'C' is not defined
>>> z=A()
obj greaterthan not 3
>>> x.a
[1, 1, 1]
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(1)
		self.a=a
		try:
			if sum(self.a)>=3:
				raise ValueError
		except ValueError:
			del self
			print "obj greaterthan not 3"

			
>>> x=A()
>>> y=A()
>>> z=A()
obj greaterthan not 3
>>> z
<__main__.A instance at 0x02B82620>
>>> del Z

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    del Z
NameError: name 'Z' is not defined
>>> del z
>>> z

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> class A:
	def __init__(self):
		self.count_def()
	def count_def(self,a=[]):
		a.append(1)
		self.a=a
		try:
			if sum(self.a)>=3:
				raise ValueError
		except ValueError:
			print self
			del self
			print "obj greaterthan not 3"

			
>>> x=A()
>>> y=A()
>>> z=A()
<__main__.A instance at 0x02BB4148>
obj greaterthan not 3
>>> z
<__main__.A instance at 0x02BB4148>
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================

Traceback (most recent call last):
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 8, in <module>
    if sum(self.a)<2:
NameError: name 'self' is not defined
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================

Traceback (most recent call last):
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 8, in <module>
    if sum(self.a)<2:
NameError: name 'self' is not defined
>>> from itertools import count
>>> x=count(0)
>>> x.next()
0
>>> x.next()
1
>>> x.next()
2
>>> x.next()
3
>>> x.next()
4
>>> x
count(5)
>>> x=count()
>>> x
count(0)
>>> x.next()
0
>>> x
count(1)
>>> x.next()
1
>>> x
count(2)
>>> x
count(2)
>>> x
count(2)
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================
[1]
1
[1, 1]
2
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================
[1]
[1, 1]

Traceback (most recent call last):
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 12, in <module>
    y=A()
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 5, in __init__
    raise ValueError
ValueError
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================
[1]
[1, 1]

Traceback (most recent call last):
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 12, in <module>
    y=A()
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 5, in __init__
    raise ValueError
ValueError
>>> z

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> y

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x
<__main__.A instance at 0x02234A80>
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================
[1]
[1, 1]
[1, 1, 1]

Traceback (most recent call last):
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 13, in <module>
    z=A()
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 5, in __init__
    raise ValueError
ValueError
>>> x
<__main__.A instance at 0x02AA28A0>
>>> y
<__main__.A instance at 0x02AD3DF0>
>>> z

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> class A:
    def __init__(self):
        self.count_def()
        if sum(self.a)==3:
            raise ValueError
    def count_def(self,a=[]):
            a.append(1)
            self.a=a

            
>>> x=A()
>>> y=A()
>>> z=A()

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    z=A()
  File "<pyshell#105>", line 5, in __init__
    raise ValueError
ValueError
>>> z

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> x
<__main__.A instance at 0x02AD3BC0>
>>> y
<__main__.A instance at 0x02AD3D00>
>>> class A:
    def __init__(self):
        self.count_def()
        try:
		if sum(self.a)>3:
			raise ValueError
	except ValueError:
		print "obj count not greaterthan 3"
    def count_def(self,a=[]):
            a.append(1)
            self.a=a

            
>>> x=A()
>>> y=A()
>>> z=A()
>>> k=A()
obj count not greaterthan 3
>>> k
<__main__.A instance at 0x02AD4558>
>>> class A:
    def __init__(self):
        self.count_def()
        if sum(self.a)>3:
		raise ValueError
    def count_def(self,a=[]):
            a.append(1)
            self.a=a

            
>>> x=A()
>>> y=A()
>>> z=A()
>>> k=A()

Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    k=A()
  File "<pyshell#120>", line 5, in __init__
    raise ValueError
ValueError
>>> k
<__main__.A instance at 0x02AD4558>
>>> l=A()

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    l=A()
  File "<pyshell#120>", line 5, in __init__
    raise ValueError
ValueError
>>> l

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================
obj count not greaterthan 3
>>> 
================= RESTART: C:/Users/Brahmaiah/Desktop/obj.py =================

Traceback (most recent call last):
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 33, in <module>
    l=A()
  File "C:/Users/Brahmaiah/Desktop/obj.py", line 24, in __init__
    raise ValueError
ValueError
>>> l

Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> x
<__main__.A instance at 0x02AF3E68>
>>> 
>>> y
<__main__.A instance at 0x02AF3C88>
>>> z
<__main__.A instance at 0x02AF2B70>
>>> 
