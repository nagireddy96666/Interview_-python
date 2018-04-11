   str1 = input("Enter a string: ")
str2 = reversed(str1)
if list(str1) == list(str2):
   print("It is palindrome")
else:
   print("It is not palindrome")
