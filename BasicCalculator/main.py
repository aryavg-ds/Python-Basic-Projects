import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

fns_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
answer = 0
f_number = int(input("Enter the first number: "))
while True:
    opr_choice = input("Enter the operation: ")
    s_number = int(input("Enter the second number: "))

    for key in fns_dict:
        if opr_choice == key:
            answer = fns_dict[key](f_number, s_number)
    print(answer)
    choice = input("Do you want to continue working with the above answer? Type 'y' or 'n': ")
    if choice == "y":
        f_number = answer
    elif choice == "n":
        choice = input("Do you want to do more calculations? Type 'y' or 'n': ")
        if choice == "y":
            f_number = int(input("Enter the first number: "))
        else:
            print("Thank you for using this program. Goodbye!")
            answer = f_number = s_number = 0
            opr_choice = choice = ""
            break
