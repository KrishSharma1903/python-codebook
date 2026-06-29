number = int(input("Enter a number: "))

digit_sum = 0

while number>0:
    remainder =  number % 10
    digit_sum += remainder
    number  =  number//10

print("The suum is : ", digit_sum)


