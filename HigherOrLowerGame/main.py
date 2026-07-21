import random

import art
import game_data

def data_retrieval(option):
    option = random.choice(game_data.data)
    name = option['name']
    followers = int(option['follower_count'])
    description = option['description']
    country = option['country']
    return name, followers, description, country

def compare_data():
    option = ()
    score = 0
    flag = True
    option_1 = data_retrieval(option)
    while flag:
        option_2 = data_retrieval(option)
        while option_1 == option_2:
            option_2 = data_retrieval(option)
        else:
            print(f"Compare A: {option_1[0]}, a {option_1[2]} from {option_1[3]}")
            print(art.vs)
            print(f"Against B: {option_2[0]}, a {option_2[2]} from {option_2[3]}")
            choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            if choice == "a":
                if option_1[1] > option_2[1]:
                    score += 1
                    print(f"You are right. Current score: {score}")
                    option_1 = option_1
                else:
                    print(f"Sorry! You are wrong. Final score: {score}")
                    flag = False
            if choice == "b":
                if option_2[1] > option_1[1]:
                    score += 1
                    print(f"You are right. Current score: {score}")
                    option_1 = option_2
                else:
                    print(f"Sorry! You are wrong. Final score: {score}")
                    flag = False


compare_data()