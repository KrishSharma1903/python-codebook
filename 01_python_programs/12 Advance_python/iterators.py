##Iterators
'''Iterators are advanced Pyhton concepts that allow for efficient looping and memory management.
Iterators provide a way to access of a collection sequentially without exposing the underlying structure'''

my_list=[1,2,3,4,5,6]
for i in my_list:
    print(i)

print(type(my_list))
print(my_list)

##iterator
iterator = iter(my_list)
print(type(iterator))
print(iterator)

##iterate through all the elemets 
print(next(iterator)) ##Done using lazy loading 
print(next(iterator)) ##We will get an error once the iterator has looped through all the elements 

##Error handling for looping after the last element 
try:
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")



# String iterator
my_string = "Hello"
string_iterator = iter(my_string)

print(next(string_iterator))  # Output: H
print(next(string_iterator))  # Output: e