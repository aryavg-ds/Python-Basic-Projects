import art
print(art.logo)

auc_dictionary = {}
highest_bid = 0
highest_bidder_name = ""
should_continue = True

# Ask the user for input
while should_continue:
    name = input("What is your name? ")

# Ensure only numeric is entered ad bid
    bid = input("What is your bid? $")
    while not bid.isdigit():
        bid = input("Please enter a number. What is your bid? $")
    bid = int(bid)

# Save data into dictionary {name: price}
    auc_dictionary[name] = bid

# Whether if new bids need to be added
    while True:
        more_bid = input("Are there any other bidders? Type 'yes' or 'no' ")
        if more_bid == "yes":
            print("\n" * 30)
            break
        elif more_bid == "no":
            should_continue = False
            break
        else:
            print("Please enter 'yes' or 'no'")
#Compare bid and print the highest
#print(auc_dictionary)
for name in auc_dictionary:
    if highest_bid < auc_dictionary[name]:
        highest_bid = auc_dictionary[name]
        highest_bidder_name = name
print(f"The highest bid is {highest_bid} by {highest_bidder_name}")
