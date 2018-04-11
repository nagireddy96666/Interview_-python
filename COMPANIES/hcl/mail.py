import re
mail=raw_input("enter the mail_id:")
x=re.split("@",mail)[0]
name=x[0]
print x
