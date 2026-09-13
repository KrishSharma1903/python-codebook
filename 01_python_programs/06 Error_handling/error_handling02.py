try:
    age = int(input("Enter your age?"))

except ValueError:
    print("Enter a valid number")
    age = int(input("Enter your age?"))


if age> 18:
    print(f"You can drive at age {age}")