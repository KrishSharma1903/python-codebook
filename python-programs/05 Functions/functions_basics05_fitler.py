def even(num):
    if num%2==0:
        return True

print(even(22))

#using filter
lst =[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even,lst)))

##Filter with a lambda function
numbers = [1,2,3,4,5,6,7,8,9]
greater_than_5 = list(filter(lambda x: x>5,numbers))
print(greater_than_5)

##Filter with lambda condition and multiple conditions
numbers = [1,2,3,4,5,6,7,8,9]
even_and_greater_than_five = list(filter(lambda x:x>5 and x%2==0,numbers))
print(even_and_greater_than_five)


##Filter( to check if the age is greater than 25 in dictonaries)
people = [
    {"name" : "Krish", "age":21},
    {"name" : "Krishna", "age":18},
    {"name" : "Dhruv", "age":28},
    {"name" : "Renit", "age":38}
]

def age_greater_than_25(person):
    return person['age']>25 

print(list(filter(age_greater_than_25,people)))