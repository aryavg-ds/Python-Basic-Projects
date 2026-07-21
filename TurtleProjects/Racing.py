from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

#basic movements
# def move_forwards():
#     tim.forward(20)
# def move_backwards():
#     tim.backward(20)
# def move_anticlockwise():
#     tim.left(10)
# def move_clockwise():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(move_forwards, "w")             # tim will move forward when w is pressed
# screen.onkey(move_backwards, "s")            # tim will move backward when s is pressed
# screen.onkey(move_clockwise, "d")            # tim will move left when d is pressed
# screen.onkey(move_anticlockwise, "a")        # tim will move right when a is pressed
# screen.onkey(clear, "c")                     # tim will clear its movements when c is pressed

#Racing Game
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race?")
color = ["red", "green", "blue", "violet", "indigo", "yellow", "orange"]
names = ["tim", "tommy", "tony", "toby", "tub", "tubby", "tuny"]
tim.hideturtle()
y_axis = [-120, -80, -40, 0, 40, 80, 120]
all_turtles = []

for j in range(len(names)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[j])
    new_turtle.penup()
    new_turtle.goto(x= -230,y= y_axis[j])
    all_turtles.append(new_turtle)
    
is_game_on = False
if user_input:
    is_game_on = True
while is_game_on:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 12)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            is_game_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_input:
                print(f"You win!! The {winning_colour} turtle wins!")
            else:
                print(f"You lose!! The {winning_colour} turtle wins!")
screen.exitonclick()
