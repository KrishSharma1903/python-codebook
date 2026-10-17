##Function copy 
##Closure
##Decorators

##Function Copy 
def welcome():
    return "Welcome!!"

print(welcome())

wel = welcome
print(wel())

del welcome
print(wel())

##Closures(Function inside a function)
def main_welcome(msg):
    def sub_welcome_method():
        print("Welcome to the sub class")
        print(msg) #can use the variable of the main function itself
        print("Please learn it")
    return sub_welcome_method()

print(main_welcome("Welcome all"))

##Closure example 2
def main_welcome(func):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func("Welcome to the tutorial")
        print("Please learn the concepts properly")
    return sub_welcome_method()

print(main_welcome(print))

##Closure example 3
def main_welcome(func,lst):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        print(func(lst))
        print("Please learn the concepts properly")
    return sub_welcome_method()

print(main_welcome(len,[1,2,3,4,5,7]))
