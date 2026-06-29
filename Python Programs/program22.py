user_input = int(input("Enter the number you want to calculate the factorial of: "))
fact = 1 
i = 1 

while i <= user_input:
    fact *=  i
    i += 1

print(fact)
