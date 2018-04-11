import re
mail="brahmaiah123abc_xyz@hotmail.com venkat@gmail.com"
x=re.search("\w+",mail)
print x.group()

