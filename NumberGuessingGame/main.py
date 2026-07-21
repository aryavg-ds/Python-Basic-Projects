import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_difficulty():
    """to set difficulty"""
    level = input("Choose a difficulty level to play. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return None

def answer_lives_check(c_numb,u_numb,life):
    """to check the number given by user"""
    if c_numb == u_numb:
        life = 0
        return life
    elif u_numb > c_numb:
        print("You are wrong. You guessed the number too high")
        life -= 1
        return life #You have 10 turns to guess the number! print outside loop
    elif u_numb < c_numb:
        print("You are wrong. You guessed the number too low")
        life -= 1
        return life


def guessing_game():
    print(art.logo)
    print("I am thinking of a number from 1 to 100"
          "\nCan you guess the number?")
    num = random.randint(1, 100)
    turns = check_difficulty()
    print(f"You have {turns} turns to guess the number!")
    is_game_over = False
    while not is_game_over:
        #To loop through the game
        u_num = int(input("Guess the number: "))
        turns = answer_lives_check(num,u_num,turns)
        if turns == 0:
            is_game_over = True
            print("Yay!! You guessed the number correctly")
        elif turns > 0:
            print(f"You have {turns} turns to guess the number!")
        elif turns < 0:
            print("Game Over!! You have no more turns to guess the number")

guessing_game()