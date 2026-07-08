MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_efficient(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quaters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost ,2)
        print(f"Here is your change{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money for the drink")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name}")
    


is_on = True

while is_on:
    order = input(
        "What drink you want? Espresso, Latte, Cappuccino: ").lower()

    if order == "off":
        is_on = False

    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif order not in MENU:
        print("Invalid drink.")

    else:
        drink = MENU[order]
        print(drink)
       
        if is_resource_efficient(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

  