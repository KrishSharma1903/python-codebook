##list compreshension
#basic syntax -> [expression  for item in iterable]
#with conditional logic -> [expression for item in iterable if condition]
#nested list compreshension -> [expression for item1 in iterable1 for item2 in iterable2]

##Basic list compreshension
lst = []
for x in range(10):
    lst.append(x**2)

print(lst)
#using list comprehension
square = [num**2 for num in range(10)]
print(square)

#using list comprehension with codition
lst = []

for i in range(10):
    if i%2==0:
        lst.append(i)

print(lst)

#using list comprehension
even_numbers = [num for num in range(10) if num%2==0]
print(even_numbers)

##nested list compreshension
lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']

pair = [[i,j] for i in lst1 for j in lst2]
print(pair)

#list comprehension with funtion calls 
words = ["Hello" , "World", "python"]
length_of_words =[len(i) for i in words ]
print(length_of_words)