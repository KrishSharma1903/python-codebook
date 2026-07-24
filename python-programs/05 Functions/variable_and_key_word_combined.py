def print_numbers(*args , **kwargs):
    for numbers in args:
        print(numbers)

    for key, value in kwargs.items():
        print(key, value)


print_numbers(1,2,3,4,5,6,7,8,9,10 , Name = "Krish", Age = 21 , Country = "India")