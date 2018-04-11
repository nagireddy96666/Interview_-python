def prime_replace():
    l=range(2,15)
    for i in l:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.insert(l.index(i),"SriRama")
            l.remove(i)
    print l
prime_replace()
