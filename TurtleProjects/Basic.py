import random
from turtle import Turtle, Screen
import turtle as T
#urls to refer:
# https://docs.python.org/3/library/turtle.html#basic-drawing
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine")

#To draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90) #90 degress angle

#To draw a dashed line
# for i in range(6):
#     tim.pendown()
#     tim.forward(10)  # draw dash
#     tim.penup()
#     tim.forward(10)
T.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    # print(color)
    return color
#To draw diff shapes from the same base with diff colours
# color = ["brown" , "purple", "blue", "green", "violet" , "aquamarine", "coral", "black"]
# for num_sides in range(4, 12):
#     angle = 360/num_sides
#     tim.color(random_color())
#     for i in range(num_sides):
#         tim.right(angle)
#         tim.forward(100)
#         continue

#To create a random walk with diff colours and path thickness
# colors = ["red", "blue", "green", "yellow", "orange",
#           "purple", "pink", "brown", "black", "gray",
#           "cyan", "magenta", "gold", "navy", "white"]


# # direction = [0 , 90, 180, 270]
# # for i in range(200):
# #     tim.speed("fastest")
# #     tim.pensize(8)
# #     tim.color(random_color())
# #     tim.setheading(random.choice(direction))
# #     tim.forward(20)
#
# #To draw a spirograph
for angle in range(0, 360, 5):
    tim.speed("fastest")
    tim.setheading(angle)
    tim.color(random_color())
    tim.circle(100)






screen = Screen()
screen.exitonclick()