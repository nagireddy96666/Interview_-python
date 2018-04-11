class MyTest:
    def __init__(self, array, upper):
        self.upper = upper;
        self.array = array

    def binary(self,n):
        lower = 0
        upper = self.upper
        while  lower <= upper:
            mid = (lower+upper)/2
            if(n < array[mid]):
                upper = mid-1
            elif(n > array[mid]):
                lower = mid+1
            elif(n == array[mid]):
                return mid
        return -1

if __name__ == "__main__":
    array = [0,1,2,3,4,5,6,7,8,9,10]
    t = MyTest(array, len(array)-1)
    x = t.binary(5)
    if x == -1:
        print "Not found"
    else:
        print "Found at", x
