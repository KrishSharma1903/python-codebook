#syntax
# lambda argument : expression

def add(a,b):
    return a+b

print(add(2,3))

##Same using the lambda function
add=(lambda a,b :a+b)
print(type(add))
print(add(5,5))

#example 2
def even(num):
    if num%2==0:
     return True
print(even(24))

even1 = lambda num : num%2==0
print(even1(12))

##Addtion of three variable
addition1 = lambda x ,y ,z : x + y + z

print(addition1(12,11,134))
