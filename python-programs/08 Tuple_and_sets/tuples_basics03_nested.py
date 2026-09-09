##nested list 
lst = [[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,'c']]
print(lst[0])
print(lst[2][1])
print(lst[1][0:2])


#nested tuple
nested_tuple = ((1,2,3),("a","b","c"),(True,False))
##accesing the element inside a tuple 
print(nested_tuple[0])
print(nested_tuple[1][2])

#iteration over nested tuple 
for i in nested_tuple:
    for items in i:
        print(items, end=" ")
    print()

