## Declaring and assigning variables

age =32
height = 6.1
name="Krish"
is_stuent =  True

##Printing the variables

print("Age:", age)
print("height:",height)
print("Name:",name)

#Naming a Variable
#1. Variables names should be descriptive
#2. They must start with a letter or an "_" and can contain letters, numbers and underscores
#3. Varivbles are case sensative

#some valid variable names

first_name = "Krish"
last_name = "Sharma"
age1 = 21

## Understadning variable types
## Pyhton is dynamically typed and type of varibale is determined at runtime 

age =32 #int 
height = 6.1 #flaot 
name="Krish" #string
is_stuent =  True #boolean

#Typechceking 
type(height) 
#Typeconversion
age = 25
type(age)
age_str = str(age)
print(type(age_str))

##Dynamic Typing 
##Pyhton allows the type of a variable to chnage as the program executes 
var = 10
print(var,type(var))

var = "Hello"
print(var,type(var))

var = 3.14
print(var,type(var))

##input
age = int(input("What is yout age?"))
print(age, type(age))

##Simple calculator 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2


print("Sum:",sum)
print("Difference:",difference)
print("Product:",product)
print("Quotient:",quotient)