def krish(s):
    if len(s) <= 1:
        return s
    return krish(s[1:]) + s[0]
s ="reddy"
print krish(s)
