import random

def deal_cards():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
          return 0
     
    if 11 in cards and sum(cards)>21:
          cards.remove(11)
          cards.append(1)

    return sum(cards)
     
def compare(user_score , computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return " You Lose, opponent has Blackjack"
    elif user_score == 0:
        return "You Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
      
def game():
    user_card = []
    computer_card = []
    computer_score = -1 
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your current cards are: {user_card}")
        print(f"Computer current cards are: {computer_card[0]}")

        if user_score == 0  or computer_score == 0 or user_score > 21:
            is_game_over = True

        else: 
            user_choice = input("Do you wann to get another card, Enter 'y' for 'yes' , else enter 'n' ").lower()

            if user_choice == "y":
                user_card.append(deal_cards())

            else:
                is_game_over = True


            
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_cards())
        computer_score = calculate_score(computer_card)


    print(f"Your final cards are{user_card} and your final score is {user_score}")
    print(f"Computer final cards are{computer_card} and computer final score is {computer_score}")


    print(compare(user_score ,computer_score))


while input ("Do you want to play another game? Press 'y' to continue ")== "y":
    print("\n"*30)
    game()

