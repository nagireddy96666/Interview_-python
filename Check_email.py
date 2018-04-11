import re
email=raw_input("Enter email id::")
def check_email(email):
    while not re.match(r"^[A-Za-z0-9]+.+[A-Za-z0-9]+@+[A-Za-z]+.+[A-Za-z]$",email):
        print "Your input is wrong Please enter valid mail Id"
        email=raw_input("Re-Enter your correct email Id::")
    print "Congrates Reddy your mail Id is valid"
check_email(email)
