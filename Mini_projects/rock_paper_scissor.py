import random

game_variabes = ["Rock" , "Paper", "Scissors"]

user_choice = int(input("Enter your choice 0: Rock, 1: Paper, 2: Scissors: "))

if user_choice >= 0  and user_choice <=2:
    print(f"You chose: {game_variabes[user_choice]}")

else: 
    print("Invalid Input")


computer_choice = random.randint(0,2)
print(f"Computer chose: {game_variabes[computer_choice]}")


if user_choice == 0 and computer_choice == 2:
    print("You Won")

elif user_choice == 2 and computer_choice == 0:
    print("Computer Won")

elif user_choice > computer_choice:
    print("You Won")

elif user_choice < computer_choice:
    print("Compter Won")

else:
    print("You tied")