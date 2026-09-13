n = int(input("Enter how many Fibonacci numbers to print: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c      