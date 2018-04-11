def Homepage():
    """home page for Library management sytm"""
    print " enter 1 for registration"
    print " enter 2 for login"
    user_choice=raw_input("enter ur choice")

def register():
    firstname= raw_input("enter ur name")
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
    print line
f=open("data.text","r")
for i in f:
    print i
f=open("data.text","a")    
f.write("line\n")
f.close()

#register()
Homepage()


    
    
    
    
