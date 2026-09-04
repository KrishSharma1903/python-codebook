##Basic set operations
#adding an element
my_set={1,2,3,4,5,6}

my_set.add(7)
print(my_set)

 #Removing an element
my_set.remove(3)
print(my_set)

# my_set.remove(200)
# print(my_set) gives a KeyError as 200 isnt in the set 

#To run without error we can use discard()
my_set.discard(200)
print(my_set)

#pop method -> Works on FIFO 
removed_element = my_set.pop()
print(removed_element)
print(my_set)

#clear all the elements 
my_set.clear()
print(my_set)

##Set membership test
my_set = {1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)