import 
def  Login():
    f=open("data.text","r")
    for line in f:
        print ','.join(line)
    login_id = str(raw_input("Enter Login ID:"))
    password = str(raw_input("Enter password:"))
    if (login_id==password):
        print "succesfully logined/n"
    else:
        print "enter password correctly \n goto registration \n"
Login()
