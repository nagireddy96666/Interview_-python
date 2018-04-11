import os
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna'):
	for i in os.listdir(root):
		if os.path.isfile(os.path.join(root,i)):
			with open(os.path.join(root,i)) as fd:
				if 'chinna' in fd.read():
					print("found")

					
found
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna'):
	for i in os.listdir(root):
		if os.path.isfile(os.path.join(root,i)):
			with open(os.path.join(root,i)) as fd:
				if 'chinna' in fd.read():
					print("found")

					
found
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna'):
	for i in os.listdir(root):
		if os.path.isfile(os.path.join(root,i)):
			with open(os.path.join(root,i)) as fd:
				if 'chinna' in fd.read():
					print("found")

					
found
found
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna')
SyntaxError: invalid syntax
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna'):
	print root

	
C:\Users\Brahmaiah\Desktop\chinna
C:\Users\Brahmaiah\Desktop\chinna\bro
C:\Users\Brahmaiah\Desktop\chinna\sis
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna'):
	print dirs

	
['bro', 'sis']
[]
[]
>>> for root,dirs,files in os.walk(r'C:\Users\Brahmaiah\Desktop\chinna'):
	print files

	
[]
['hello.txt', 'hello1.txt']
['ram.txt']
