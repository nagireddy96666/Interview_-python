print('!* To Find Python Armstrong Number')
def Armstrong_Number():
    num = input('Enter Number to check for Armstrong')
    digit = input('Your Entered number is of how many digits')
    n = num
    sum = 0		
    while(n!=0):
        r = n % 10
        n = n / 10
        sum = sum + ( r ** digit)
        
    if( sum == num):
        print('%d is a armstrong number' %num)
    else:
        print('%d is not a armstrong number' %num)
Armstrong_Number()
