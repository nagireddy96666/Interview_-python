import re
str="8978878020"#expected out put:'897-887-802-0'
x=re.findall("\d{1,3}",str)
print x
y="-".join(x)
print y
print "format"
print('{:,}'.format(111222333))
