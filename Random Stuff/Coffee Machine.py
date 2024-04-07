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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

revenue = 0

def check_resource(order_ingredients):
    """Returns true if order can be made due to the availability of resource and false if it can't be made"""
    """Returns ingredients as a key value pair in a dictionary format from the menu"""
    """Also we are not trying to return the individual value, we just want to figure out if there is enough resources"""
    """Item will iterate over the key and not the value, which is why when we take the dictionary of order_ingredients[item]"""
    """It will return the amount that it has, then comparing it to resources[item] which gives the value pair in the resource dict"""

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            return True
    """If this returns True, we can then start the payment process, otherwise it will return the above"""

def process_money():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns true when payment is successful, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        """User change rounded to 2 Decimal Places"""
        print(f"Here is your change: ${change}")
        global revenue
        """Have to tap into the global variable (scope) because we wanted to refer to it later on"""
        revenue += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino?: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${revenue}")
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, drink['cost']):
                """The drink variable allows us to access both the ingredient and cost dictionaries"""
                """Above, we access the cost for our is_transaction_successful function to work"""
                """And below, we access the ingredient for our coffee making function to work"""
                make_coffee(choice, drink['ingredients'])