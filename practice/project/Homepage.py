def Home_page():

    """
        LMS  Homepgae
    """
    print "if u already registered please Login\n else goto Registration"
    
    "required position environment"

    print "1.Registration"
    print "2.login"
    print "3.admin"
    print "4.books"
    print "5.mail confirmation"
    print "6.exit"
    enter_user_choice = raw_input("Enter User Choice")
    if int(enter_user_choice) == 1:
        register()
    elif int(enter_user_choice) == 2:
        Login()
    elif int(enter_user_choice) == 3:
        print "Enter into admin module"
    elif int(enter_user_choice) == 4:
        print "Entered into books module"
    elif int(enter_user_choice) == 5:
        print "Entered into mail forward"
    elif int(enter_user_choice) == 6:
        print "Entered into exit"
def register():
    firstname= raw_input("enter ur name")
#while(type(firstname)!=str):
#print " enter valid name"
#break;
    lastname= raw_input("enter ur last name")
    email= raw_input("enter ur email")
    mobile_number= raw_input("enter ur mobile number")
    address= raw_input("enter ur address")
    address2= raw_input("enter ur address2")
    user_id= raw_input("enter ur user id")
    password= raw_input("enter ur password")
    confirm_password= raw_input("enter ur confirm password")
    l=[]
    l.append(firstname)
    l.append(lastname)
    l.append(email)
    l.append(mobile_number)
    l.append(address2)
    l.append(address2)
    l.append(user_id)
    l.append(password)
    l.append( confirm_password)
    print l
    line = ','.join(l)
    #print line
    s=str(line)
    print s
    f=open("data.text","a")
    d= f.write(s)
    print d
    f.close()
def  Login():
    login_id = raw_input("Enter Login ID:")
    password = raw_input("Enter password:")
    if (login_id==password):
        print "succesfully logined"
    else:
        print "enter password correctly\n again login with correct details"

    
#Calling Home page
Home_page()

                         
