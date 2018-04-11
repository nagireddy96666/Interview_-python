with open("text2.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        a=line.split('\t')
        if "hai" in a:
            print a
