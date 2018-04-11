chars = words = lines = 0
with open("data.text", 'r') as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)
        print lines,words,chars
