total= 0
while True:
    user_input = int(input("Enter a number:"))
    if user_input == 0:
        break
    else:
        total += user_input


print(total)