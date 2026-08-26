def square(x):
    return x*x

numbers = [1,2,3,4,5,6,7,8]
print(list(map(square,numbers)))


##Lambda function with map
numbers = [1,2,3,4,5,6,7,8]
print(list(map(lambda x: x*x,numbers)))

##map multiple iteratable
numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers= list(map(lambda x,y : x+y,numbers1,numbers2))
print(added_numbers)

#map() to convert a list of strings to intergers
str_numbers = ['1','2','3','4','5']
int_numbers = list(map(int,str_numbers))
print((int_numbers))

#example 
words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.upper,words))
print(upper_words)

#example 
def getname(person):
    return person["name"]

people = [
    {"name" : "Krish", "age":21},
    {"name" : "Krishna", "age":18}
]
print(list(map(getname, people)))