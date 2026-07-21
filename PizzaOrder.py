print("Welcome to Python Pizza Deliveries!")
pizza_cash = 0
size = input("What size pizza do you want? S, M or L: ").upper()
if size == "S" :
    pizza_cash = 15
elif size == "M" :
    pizza_cash = 20
elif size == "L" :
    pizza_cash = 25
else:
    print("Sorry, please enter either 'S' or 'M' or 'L'")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if (pepperoni == "Y") and (size == "S" ):
    pizza_cash += 2
elif (pepperoni == "Y") and (size == "M" or "L" ):
    pizza_cash += 3
elif pepperoni == "N" :
    print("No Pepperoni!")
else:
    print("Sorry, please enter either Y or N")
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y" :
    pizza_cash += 1
elif extra_cheese == "N" :
    print("No extra cheese!")
else:
    print("Sorry, please enter either Y or N")
print(f"The total cost is ${pizza_cash}")

