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
"""Objectives
Prompt user by asking, 'what would you like'
Turn off the coffee machine by entering 'off' to the prompt
Print report
Check resources are sufficient
Process coins
Create successful transactions
Make coffee"""

def sufficient_resource(order_ingredients):
    """returns true when order can be created based on resources being enough"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry you do not have enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """Returns total amount of coins deposited"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(money_recieved, drink_cost):
    """Returns true when payment is accepted or False is insufficient money"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"You have ${change} in change. Here you go!")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money refunded.")
        return False

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ")

is_on = True

while is_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if sufficient_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
