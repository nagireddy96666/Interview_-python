with open("data.text", "r") as f:
    f = f.readlines()
    print f
    d=''.join(f)
    print d
    g=d.split()
    for i in enumerate(g):
        print i
    array = []
    for line in f:
        array.append(line)
