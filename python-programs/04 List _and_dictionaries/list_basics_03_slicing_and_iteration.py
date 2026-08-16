##Slicing list
numbers = [1,2,3,4,5,6,7,8,9,10] 

print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

##Iteration in list 

for i in numbers:
    print(i)

#Iteration with index

for index, i in enumerate(numbers):
    print(index,i)

#enumerate is a inbuilt function used to print the indexes with the elements in the list 