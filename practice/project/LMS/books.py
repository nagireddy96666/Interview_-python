def Books():

    """
        Books  Homepgae
    """
    print "select required book and inform to admin"
    
    "RequiredType Of Books"
    print "1.Engineering"
    print "2.science"
    print "3.hisrory"
    print "4.exit from library"
    enter_user_choice = raw_input("Enter User Choice")
    if int(enter_user_choice) == 1:
       Engineering()
    elif int(enter_user_choice) == 2:
       science()
    elif int(enter_user_choice) == 3:
        history()
    elif int(enter_user_choice) == 4:
       exit()
def Engineering():
    print" enter into CSE department books"
    print" enter into EEE department Books"
    print" enter into IT department books"
    print" enter into MECH department books"
def science():
    print" enter into geo department books"
    print" enter into BIO epartment Books"
    print" enter into ENVIRONMENTAL department books"
def history():
    print" enter into POLITY partment books"
    print" enter into BUSINESS department Books"
    print" enter into IT department books"
    
Books()      
