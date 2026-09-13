##List 
fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]
#append -> add an item to the end 
fruits.append("orange")
print(fruits)

#insert -> used to add element to a speicific index 
fruits.insert(1,"watermelon")
print(fruits)

#remove -> to remove the first occurance of an item 
fruits.remove("Banana")
print(fruits)

#pop -> remove and return the last 
pop_fruit = fruits.pop()
print(pop_fruit)
print(fruits)

#index -> print index of a specific element 
index = fruits.index("Cherry")
print(index)

#counts -> counts the number of occurance of a specific element 
fruits.insert(2,"watermelon")
print(fruits)
print(fruits.count("watermelon"))

#sort -> sorts the elements of list in ascending order 
fruits.sort()
print(fruits)

#reverse -> reverses the list
fruits.reverse()
print(fruits)

#clear -> removes all the elements from the list 
fruits.clear()
print(fruits)