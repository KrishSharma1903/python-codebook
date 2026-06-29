print(" Welcome to the pizza delivery ")
size = input("What size of pizza do you want s:small, m: medium, l:large ").lower()
pepperoni= input("DO you want to add extra pepperoni to it. 'Y' for yes and 'n' for no: ").lower()
extra_cheese = input("Do you want extra cheese 'Y' for yes and 'n' for no: ")

bill = 0 

if size == 's':
    bill += 150
elif size == 'm':
    bill += 250
elif size == 'l':
    bill += 350
else:
    print("Invalid size")

if pepperoni == "y":
    if size == "s":
        bill+= 50
    else:
        bill+= 70

if extra_cheese == "y":
    bill+= 80

print(f"Your total bill is: {bill}")
