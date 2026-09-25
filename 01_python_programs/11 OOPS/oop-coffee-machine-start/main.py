from menu import Menu 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_choice = input((f"What would you like to get? {options}"))
    
    if user_choice == 'off':
        is_on = False
    
    elif user_choice == "report":
        moneymachine.report()
        coffeemaker.report()
    
    else:
        drink = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)