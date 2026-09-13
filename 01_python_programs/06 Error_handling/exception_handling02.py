#To catch any exception by using the Exception class
try:
    result=1/2
    # a=b
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
except Exception as ex1:
    print(ex1)
    print('Main exception got caught here')


#Example 
try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex:
    print(ex)


