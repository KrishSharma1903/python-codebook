#Understanding Exceptions
'''Exception handling in Python allows you to handle errors gracefully and take corrective actions without stopping the execution of the program. This lesson will cover
 the basics of exceptions, including how to use try, except, else, and finally blocks.'''

# What Are Exceptions?
# Exceptions are events that disrupt the normal flow of a program. They occur when an error is encountered during program execution. Common exceptions include:

# ZeroDivisionError: Dividing by zero.
# FileNotFoundError: File not found.
# ValueError: Invalid value.
# TypeError: Invalid type.

# a=b -> this will throw a NameError as b is not defined
#for exception handling we will use try,except block
# try:
#     #  a=b
# except:
#      print("Variable isn't assigned")

#Priting the error 
# try:
#      a=b
# # except NameError as ex:
#      print(ex)


#Handling divide by zero error
try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")

