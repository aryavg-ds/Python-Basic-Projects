from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

options = menu.get_items()  #Returns all the names of the available
                                # menu items as a concatenated string.e.g. “latte/espresso/cappuccino”

flag = True
while flag:
    choice = input(f"What would you like? {options} : ").lower()
    if choice == "off":
        flag = False
    elif choice == "report":
        # to print report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
