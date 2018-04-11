import re
sentence = 'we are humans'
matched = re.match(r'(.*) (.*) (.*)', sentence)
print(matched.groups())#groups separately

sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.group())#group together
