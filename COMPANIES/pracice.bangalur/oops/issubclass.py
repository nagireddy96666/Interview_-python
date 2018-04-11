#issubclass(child,parent)

class a:
    pass
class b(a):
    pass
class c(b):
    pass

print(issubclass(c,b))#it returns true
print(issubclass(b,c))#it returns false
