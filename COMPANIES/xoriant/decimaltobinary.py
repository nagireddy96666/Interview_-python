def intToBin(n):
    nums = [n]
    while n > 1:
        n = n // 2
        nums.append(n)

    bits = []
    for i in nums:
        bits.append(str(0 if i%2 == 0 else 1))
    bits.reverse()
    print ''.join(bits)
intToBin(15)
'''
def intToBin(n):
    bits = []

    bits.append(str(0 if n%2 == 0 else 1))
    while n > 1:
        n = n // 2
        bits.append(str(0 if n%2 == 0 else 1))

    bits.reverse()
    return ''.join(bits)
'''
http://pythontutor.com/visualize.html#mode=display

def f(n):
	if n>1:
		f(n//2)
	print(n%2,)

	
