people = [
    {"name" : "Krish" , "age": 21},
    {"name" : "Krishna" , "age": 18},
    {"name" : "John" , "age": 30},
]

def age_greater_than_18(x):
    return x['age']>18


print(list(filter(age_greater_than_18 , people)))