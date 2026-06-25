print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? ")) 
age = int(input("Enter your age: "))

if height > 120:
    print("You can ride the roller coaster!!")
    
    if age<=12:
        print("Your ticket price is 700")
    elif age<=18:
        print("Your ticket price is 1200 ")
    else:
        print("Your ticket price is 1600 ")

else:
    print("You need to grow up bvefore you can ride")