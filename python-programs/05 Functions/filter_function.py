def even(num):
    if num % 2 == 0:
        return True 
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = (list(filter(even,lst))) 

# print(lst1)

#problem 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_five = list(filter(lambda x : x > 5 , numbers))

# print(greater_than_five)


#problem 3
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_five_and_even = list(filter(lambda x : x > 5 and x % 2 == 0 , numbers1))
print(greater_than_five_and_even)

