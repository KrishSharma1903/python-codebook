print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? ")) 
age = int(input("Enter your age: "))
bill = 0

if height > 120:
    print("You can ride the roller coaster!!")
    
    if age<=12:
        bill = 700
    elif age<=18:
       bill = 1200
    else:
      bill = 1600

    pic = input("Do you want a picture for the ride? Enter 'y' for yes and 'n' for no \n")
    if pic == 'y':
        bill+= 300
    print(f"Your total bill is {bill}")

else:
    print("You need to grow up before you can ride")