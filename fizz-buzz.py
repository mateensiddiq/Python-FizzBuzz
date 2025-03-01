#This is the Fizz Buzz problem. This code will print our numbers 1 - 100. 
#But, if a number is a multiple of 3, we print Fizz.
#If a number is a multiple of 5, we print Buzz.
#If a number is a multiple of both 3 and 5, then we print FizzBuzz
x = int(input("What is the start number of FizzBuzz?"))
n = int(input("What is the end number of FizzBuzz?"))

for i in range(x,n+1):

    if(i%3==0 and i%5==0):
        print("FizzBuzz")

    elif(i%3==0):
        print("Fizz")

    elif(i%5==0):
        print("Buzz")
        
    else:
        print(i)