import os
for file in os.listdir("C:\Users\Dell\Desktop\ms word"):
    if file.endswith(".doc"):
        print(file)
