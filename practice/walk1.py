import os
for root, dirs, files in os.walk("C:\Users\Dell\Desktop"):
    print root
    print dirs
    print files
    for file in files:
        if file.endswith('.docx'):
            print file
