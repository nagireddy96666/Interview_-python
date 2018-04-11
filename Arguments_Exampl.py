def arguments(a,b=10,*args,**kwargs):
    print a,b,args,kwargs
arguments(10)
arguments(10,100)
arguments(00,10,20,30,40,45,x=50,y=60)
