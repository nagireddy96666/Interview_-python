try:
    file=open('sample.txt','r+')
    x=file.write('123')
    file.close()
except:
    file=open('sample.txt','w')
    x=file.write('456')
    file.close()

    
