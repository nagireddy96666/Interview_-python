import string

def main():
    print "Program determines the number of lines, words and chars in a file."
    name = raw_input("What is the file name to analyze? ")

    f= open("data.text", 'r')
    data = f.read()

    words = string.split(data)

    chars = 0
    lines = 0
    for i in words:
        chars = chars + len(i)

    print chars, len(words)


main()
