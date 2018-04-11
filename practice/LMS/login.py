def Register():
    data = []
    name = raw_input("Enter Your Name:")
    while type(name) != str:
        print "Enter valid name"
        name = raw_input("Enter Your Name:")
    data.append(name)
    
    email = raw_input("Enter Your email:")
    data.append(email)
    mobile = raw_input("Enter Your mobile number:")
    data.append(mobile)
    password = raw_input("Enter Your password:")    
    confirm_password = raw_input("Confirm Your password:")
    data.append(password)
    line = ",".join(data) +"\n"
    
    f= open("userdata.txt","a")
    f.write(line)
    f.close()
    
def login_func(username,password):
    f= open("userdata.txt","r")
    lines = (f.read()).split("\n")
    f.close()
    for line in lines:
        if username==line.split(",")[0]:
            if password==line.split(",")[-1]:
                print "Lgged in successfully"
                return 1
    else:
        print "Enter valid details"
        return 0
        
