import login
import books
print "For Login Enter 1\n"
print "For new registration Enter 2\n"
print "========================"
print "========================"

user_input = int(raw_input("Enter User Choice:"))
print type(user_input),int(user_input)


while int(user_input) !=1 and int(user_input)!=2:
    print "Entered Wrong Choice please enter 1 or 2\n"
    user_input = int(raw_input("Enter User Choice:"))
    
if int(user_input) == 1:
    print "Plese Enter user name and password"
    username = raw_input("Enter user name:")
    password = raw_input("Enter password")
    res = login.login_func(username,password)

    choice =3
    while choice:
        if res:
            break
        else:
            choice -=1
            username = raw_input("Enter user name:")
            password = raw_input("Enter password")
            res = login.login_func(username,password)
    else:
        print "You tried max number if times please after 3 mnts"
        
elif int(user_input) == 2:
    print "Please fill the Registartion Form"
    login.Register()
    print "Registere Successfully"
elif int(user_input) == 3:
    print "Plese select books from the department" 
books.Books() 

