#Tuple Operation
numbers = (1,2,3,4,5,6)
mixed_tuple = (1,"Hello World", 3.14, True)

#concatination
print(numbers+mixed_tuple)

#multiply operation
print(numbers*3)

##Immutable nature of tuples
#tuples are immutable, meaning their elements cannot be changed once assigned 
lst=[1,2,3,4,5]
print(lst)
lst[1]="Krish"
print(lst)

# numbers[2]="Krish"   #TypeError

##Tuple methods
#count() -> counts the number of occurrance of the element
#index() -> returns the index of the first occurance of a specific element 
numbers = (1,2,2,3,4,5,6)
print(numbers.count(2))
print(numbers.index(2))


##Packing tuples
packed_tuple = 1,"Hello",3.14 #-> if we initalize like this then the elements are stored in a tuple
print(packed_tuple)

##Unpacking tuples
a,b,c=packed_tuple
print(a)
print(b)
print(c)

##Unpacking with *
numbers =(1,2,3,4,5,6)
first, *middle, last =numbers
print(first)
print(middle)
print(last)