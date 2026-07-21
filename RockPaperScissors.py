import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_rps = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissors game!\n")
user_inp = input("What do you choose? \n "
                "Type 0 for rock, 1 for paper, 2 for scissors: \n ")
if user_inp not in ["0", "1", "2"]:
    print("Invalid option chosen. You lose!")
else:
    rps_user = int(user_inp)
    rps_computer = random.randint(0,2)
    print("You chose:\n", list_rps[rps_user])
    print("Computer chose:\n", list_rps[rps_computer])
    if rps_user == rps_computer:
        print("It's a draw!")
    else:
        if rps_user == 0 and rps_computer == 1:
            print("Paper covers Rock, You lose!")
        elif rps_user == 0 and rps_computer == 2:
            print("Rock smashes Scissors, You win!")
        elif rps_user == 1 and rps_computer == 0:
            print("Paper covers Rock, You win!")
        elif rps_user == 1 and rps_computer == 2:
            print("Scissors cut Paper, You lose!")
        elif rps_user == 2 and rps_computer == 0:
            print("Rock smashes Scissors, You lose!")
        elif rps_user == 2 and rps_computer == 1:
            print("Scissors cut Paper, You win!")
