#Default parameters 
def greet(name = "user"):
  print(f"Hello {name}")

greet()

##Variable length argument 
#postional argument 

def print_numbers(*args):
  for numbers in args:
    print(numbers)

print_numbers(1,2,3,"Krish")

#keyword argument (all parameters will be in form of key value pairs)
def print_detail(**kwargs):
  for key , value in kwargs.items():
    print(f"{key}:{value}")

print_detail(name="Krish", age=32,country="India")

#Positinal and Keyword argument 
def print_detail(*args,**kwargs):
  for val in args:
    print(f"Positional argument : {val}")

  for key , value in kwargs.items():
    print(f"{key}:{value}")

print_detail(1,2,3,"Krish",name="Krish", age=32,country="India")


#return statement 
def multiply(a,b):
  return a*b

print(multiply(2,3))
