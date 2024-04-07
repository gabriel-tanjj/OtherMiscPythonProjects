from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

money_tracker = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_coffee_maker_on = True

while is_coffee_maker_on:

    """Options help us get the list of menu items for our f string input"""
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    """Breakdown of code below"""
    """Off for technician and maintenance guy"""
    """Report for whoever wants to see how much resources there are in the cofee maker"""
    """If any other input is triggered, you get the drink and its associated resources needed"""
    """you then use the is_resource_sufficient method to return a true / false """
    """Then use the make_payment method to process coins AND check if the amount put in is enough and process change"""
    """If both is_resource_sufficient and make_payment = true, we make the coffee"""
    if choice == "off":
        is_coffee_maker_on = False
    elif choice == "report":
        coffee_maker.report()
        money_tracker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_tracker.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


