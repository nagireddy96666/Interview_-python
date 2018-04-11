states={'ap':'andhra','ts':'telangana'}
print states
>>> def fruitfunc():
	print "this is fruit function:"

	
>>> def vegtablefunc():
	print "this is vegitabe function"

	
>>> d={'fruit':fruitfunc,'vegitable':vegtablefunc}
>>> d
{'fruit': <function fruitfunc at 0x02937030>, 'vegitable': <function vegtablefunc at 0x02937AF0>}
>>> d['fruit']
<function fruitfunc at 0x02937030>
>>> d['fruit']()
this is fruit function:
>>> d={'fruit':fruitfunc(),'vegitable':vegtablefunc()}
this is fruit function:
this is vegitabe function
>>> l=(('aa',1),('bb',2),('cc',3),('dd',4),('ee',5),('ff',6))
>>> l
(('aa', 1), ('bb', 2), ('cc', 3), ('dd', 4), ('ee', 5), ('ff', 6))
>>> x=dict(l)
>>> x
{'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4, 'ee': 5, 'ff': 6}
>>> x.items()
[('aa', 1), ('bb', 2), ('cc', 3), ('dd', 4), ('ee', 5), ('ff', 6)]
>>> x.keys()
['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
>>> x.items()
[('aa', 1), ('bb', 2), ('cc', 3), ('dd', 4), ('ee', 5), ('ff', 6)]
>>> x.values()
[1, 2, 3, 4, 5, 6]
>>> x.has_key('bb')
True
>>> x.has_key('b')
False
>>> print x['cc']
3
>>> print x['c']

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print x['c']
KeyError: 'c'
print x.get('c')
None

