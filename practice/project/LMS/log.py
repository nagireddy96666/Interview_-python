
    f= open("userdata.txt","r")
    lines = (f.read()).split("\n")
    f.close()
    for line in lines:
        if username==line.split(",")[0]:
            if password==line.split(",")[-1]:
                print "Lgged in successfully"
                            
