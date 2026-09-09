#creating a tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

lst= list()
print(type(lst))
tup = tuple()
print(type(tup))

#tuple with elements 
numbers = tuple([1,2,3,4,5,6])
print(numbers)

#mixed tuple
mixed_tuple = (1,"Hello World", 3.14, True)
print(mixed_tuple)

#Accessing tuple elements
numbers = (1,2,3,4,5,6)
print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[0:4])