import urllib2
import urllib
response=urllib2.urlopen('http://pythonforbeginners.com/')
print response.info()
html=response.read()
print html
response.close()
