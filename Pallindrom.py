def palindrome(a):
     b=a[::-1]
     if a==b:
       return "Palindrome"
     else:
       return "Not Palindrome"
a=raw_input('Enter :')
print palindrome(a)



