#if statement 
age = 20 

if age >= 18:
    print("You are allowed to voted in the elections")

##else statement 
# The else statment executes a block of code if the condition in the if statement is false.

age = 16

if age >= 18:
    print("You are allowed to voted in the elections")

else:
     print("You are not allowed to voted in the elections")
    

#elif statement (else-if)
#elif allows to check for multiple statements 
age = 20

if age<13:
    print("You are a child")

elif age<18:
    print("You are a teenager")

else:
    print("You are a adult") 


##nested if else 
#Check whether the number is odd, even or negative 
num = int(input("Enter the number: "))

if num>0:
    print("The number is positive")

    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

else:
    print("The number is zero or negative")


