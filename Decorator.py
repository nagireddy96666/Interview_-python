

def call(*args):
    def call_fn(fn):
        return fn(*args)
    return call_fn
@call(9)
def table(n):
    value = []
    for i in range(n):
        value.append(i*i)
    return value
a=len(table), table[3]
print a

