x=raw_input("enter a strin:")
#ch=raw_input("enter a occurance to find no of occurancces")
count=0
for i in x:
    if i in "aeiou":
        count=count+1
print count
