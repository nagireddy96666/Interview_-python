import re
"""
m='97392212899'
phone_re = re.match(r'\d{10}$',m)
print phone_re

a="+99-9701236632"
b=re.match(r'(^[+0-9]{1,3})-*([0-9]{10,11}$)',a)
print b"""

a="lakshma.arikatla1988@gmail.com"
b=re.match(r"^[A-Za-z0-9]+.+[A-Za-z0-9]+@+[A-Za-z]+.+[A-Za-z]$",a)
print b

a="192.168.0.121"
IP=re.match(r"^\d{1,3}\.\d{1,3}\.\d{0,1}\.\d{1,4}$",a)
print IP

#below pattern featch all the words ends with reddy
s='lakshmareddy venkat srinu ramireddy ramesh jyothi pereddy raju kotireddy'
s1=re.findall("\w+reddy",s)
print s1
