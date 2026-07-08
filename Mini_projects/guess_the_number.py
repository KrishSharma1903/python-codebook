import random

HARD_LEVEL_GAME = 5
EASY_LEVEL_GAME = 10


def rules(guess, number, turn):
    if guess > number:
        print("You guessed too high.")
        return turn - 1
    elif guess < number:
        print("You guessed too low.")
        return turn - 1
    else:
        print("You guessed the right number!!")
        return turn        




def set_difficulty():
    choice= input("Enter the difficulty level you want to play, PRESS 'H' FOR HARD AND PRESS 'E' FOR EASY: ").lower()
    if choice == "h":
        return HARD_LEVEL_GAME
    else:
        return EASY_LEVEL_GAME

def game():
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("I AM THINKING OF A NUMBER BETWEEN 1 TO 100")

    number = random.randint(1,100)
    print(number)

    turn = set_difficulty()

    guess = 0

    while guess != number:
        print(f"You have {turn} number of lives remaining") 
        guess = (int(input("Enter the number you want to guess: ")))
        turn =  rules(guess,number,turn)

        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


game()

