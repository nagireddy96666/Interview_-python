fname = "data.text"
num_lines = 0
num_words = 0
num_chars = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
