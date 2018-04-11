l=[6,1,6,9,6,8,9,12]

for i in l:
    for j in l:
        for k in l:
            if i+j+k==30:
                print "%d+%d+%d=%d"%(i,j,k,i+j+k)
                break

