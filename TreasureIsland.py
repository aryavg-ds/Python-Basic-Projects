print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
lor = input("Which do you choose? Left or Right").lower()
if lor == "right":
    print("Oops! You fell into a hole! Good luck next time! Game Over!")
elif lor == "left":
    sow = input("Okay, Do you want to swim or wait?").lower()
    if sow == "swim":
        print("Oops! You got attacked by a trout! Better Luck next time...Game over!")
    elif sow == "wait":
        rby = input("Which door do you want to open? Red, Blue or Yellow?").lower()
        if rby == "red":
            print("Oops! You just got burned by fire! Better luck next time.. Game Over!")
        elif rby == "blue" :
            print("Oops! You just got eaten by beasts! Better luck next time.. Game Over!")
        elif rby == "yellow" :
            print("Yay! You found the treasure.. Congratulations!! You won the game!!!")
        else:
            print("You chose the wrong input.. Game Over!")
    else:
        print("You chose the wrong input.. Game Over!")
else:
     print("You chose the wrong input.. Game Over!")



