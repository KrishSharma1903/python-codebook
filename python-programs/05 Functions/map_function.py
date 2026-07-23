def square(x):
    return x*x

numbers = [1,2,3,4,5,6,7,8]

# print(list(map(square, numbers)))




# using lambda
# print(list(map(lambda x : x*x , numbers))

number1 = [1,2,3,4,5]
number2 = [6,7,8,9,10]

print(list(map(lambda x, y : x  + y , number1 , number2)))
