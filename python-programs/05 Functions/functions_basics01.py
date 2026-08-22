#Why functions
def even_or_odd(num):
    if num%2==0:
     print("Even")
    else:
     print("Odd")

even_or_odd(23)
even_or_odd(32)
#Functions allow reuseability of code 

##Functions with multiple parameters

def add(num1,num2):
  return num1+num2

result = add(12,2)
print(result)

