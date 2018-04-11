a=[2,4,"Reddy","Lakshma",5,6,23,"Arikatla",12]
b=[]
def get_avg():
    for i in a:
        if type(i)==int:
            b.append(i)
    print b
    avg=sum(b)/len(b)
    print avg
get_avg()
