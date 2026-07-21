import data
profit = 0

def money_calc (quarter, dime, nickle, penny, cost):
    total = ((quarter * 25) + (dime * 10) + (nickle * 5) + (penny * 1)) / 100
    if total >= cost:
        balance = total - cost
    else:
        balance = -2.0
    return balance

def data_retrieval(choice):
    option = {}
    if choice == "espresso":
        option = data.MENU["espresso"]
    elif choice == "latte":
        option = data.MENU["latte"]
    elif choice == "cappuccino":
        option = data.MENU["cappuccino"]
    return option

def remaining_resource(resource, ingredient):
    resource = resource
    ingredient = ingredient
    for item in ingredient:
        resource[item] -= ingredient[item]
    return resource

def check_resource(resource, ingredient):
    for item in ingredient:
        if resource[item] < ingredient[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def main_fn():
    global profit
    flag = True
    while flag:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice not in ["off" , "report"]:
            option = data_retrieval(choice)
            resources = data.resources
            ingredient = option["ingredients"]
            if not check_resource(resources, ingredient):
                continue
            remaining_resource(resources, ingredient)
            quarter = float(input("Please insert coins.\nHow many quarters?"))
            dime = float(input("How many dimes?"))
            nickle = float(input("How many nickles?"))
            penny = float(input("How many pennies?"))
            cost = float(option["cost"])
            balance = money_calc(quarter, dime, nickle, penny, cost)
            if balance == 0.0:
                profit += cost
                print(f"Here is your {choice}. Enjoy!")
            elif balance == -2.0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += cost
                print(f"Here is the balance of ${balance:.2f} in change."
                        f"\nHere is your {choice}. Enjoy!")
        elif choice == "report":
            print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}"
                  f"\nCoffee: {resources["coffee"]}\nMoney: {profit}")
        elif choice == "off":
            flag = False
main_fn()
