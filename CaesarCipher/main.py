import logo
print(logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Enter correct direction to continue")
        continue

    text = input("Type your message:\n").lower()

    shift = input("Type the shift number:\n")
    while not shift.isdigit():
        shift = input("Please enter numbers only: ")

    shift = int(shift)
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    while True:
        restart = input("Would you like to code again? Type 'y' or 'n':\n").lower()
        if restart == "y":
            break
        elif restart == "n":
            should_continue = False
            print("Goodbye then!")
            break
        else:
            print("Please enter a valid input\n")

