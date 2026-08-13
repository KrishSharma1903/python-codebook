##Introduction to lists
# They are ordered, mutable collection of items.
# They can contian items of different data types

#defining a list 
lst = []
print(type(lst))

#Giving elements to the list
names = ["Krish", "Jack", "Jacob",1,2,3,4,5] 
print(names)

#mixed list 
mixed_list = [1,"Hello",3.14,True]
print(mixed_list)

#Accessing list elements
fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]
print(fruits[0])
print(fruits[2])
print(fruits[-1])

#other way of priniting 
print(fruits[1:])
print(fruits[1:3])
print(fruits[-1:])

#Modifying the list elements
fruits[1] ="Watermelon"
print(fruits)

fruits[1:]="Watermelon"
print(fruits)


