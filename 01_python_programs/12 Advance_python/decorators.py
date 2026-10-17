# Decorators
''' Decorators are a powerful and flexible feature in Python that allows you to modify the behavior of a function or class method. 
They are commonly used to add functionality to functions or methods without modifying their actual code. '''

##Decoraters
def main_welcome(func):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("Please learn the concepts properly")
    return sub_welcome_method()

@main_welcome #decorater 
def course_intro():#goes under main_welcome as a parameter
    print("This is a advance py course")


##EXAMPLE 2
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

##EXAMPLE 3(Decoraters with arguments)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()