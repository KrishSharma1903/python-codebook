# def unique_numbers(numbers):
#     new = list(set(numbers))
#     return new 

# lst = [1,1,1,1,2,3,4,5,6,7,7,8,8,9]
# print(unique_numbers(lst))



# or 


lst_1 = [1,1,1,1,2,3,4,5,6,7,7,8,8,9]
lst_2 = []

for i in lst_1:
    if i not in lst_2:
        lst_2.append(i)

print(lst_2)
