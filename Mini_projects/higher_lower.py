from higher_lower_data import data
import random


def options(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def game_rules(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'
    
game_over = False
game_score = 0
account_a = random.choice(data)
account_b = random.choice(data)

while account_a == account_b:
    account_b = random.choice(data)
while not game_over:
    print(f"The first account {options(account_a)}")
    print("vs")
    print(f"The second account {options(account_b)}")

    user_choice = input(f"Who has more followers? " f"Type 'a' for {account_a['name']} or 'b' for {account_b['name']}: ").lower()

    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    answer = game_rules(user_choice, followers_a, followers_b)

    if answer:
        game_score += 1
        print(f"Correct! Your score is {game_score}")
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
    else:
        print(f"Wrong! Final score: {game_score}")
        game_over =True





        
