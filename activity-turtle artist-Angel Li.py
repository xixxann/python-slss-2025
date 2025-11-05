# Turtle Artist
# Author: Angel Li
# 28 October

# Using turtle to draw a recurisve pattern of flower petals to form a geometric flower

import turtle


wn = turtle.Screen()
t = turtle.Turtle()
wn.bgcolor("lightblue")

# set up turtle
t.pensize(5)
t.shape("turtle")
t.color("pink")
t.pendown()

# get petal colours
PETAL_COLOURS = {
    # blues
    "cerulean": "#247BA0",
    "pale azure": "#90D7FF",
    "aquamarine": "#5DFDCB",
    "cornflower blue": "#5C95FF",
    # yellows
    "sunglow": "#FDCA40",
    # purples
    "dark purple": "#592E83",
    "purple": "#9984D4",
    "vibrantpurple": "#B27EEA",
    "lightpurple": "#CAA8F5",
}


def draw_one_petal(petal_number: int, petal_length: float):
    """Draws one petal based on the petal number and petal length
    Turtle starts from the middle of the flower and points south"""
    if petal_number == 4:
        t.goto(0, 0)
        t.color(PETAL_COLOURS["sunglow"])
        t.shape("circle")
        t.stamp()
    else:
        for _ in range(petal_number):
            t.begin_fill()
            t.color(PETAL_COLOURS["dark purple"])
            t.forward(petal_length)
            t.left(360 / petal_number)
            t.color(PETAL_COLOURS["purple"])
            t.forward(petal_length)
            t.left(180 - (360 / petal_number))
            t.color(PETAL_COLOURS["cornflower blue"])
            t.forward(petal_length)
            t.right(180 - (360 / petal_number))
            t.backward(petal_length)
            t.color(PETAL_COLOURS["lightpurple"])
            t.end_fill()


def draw_flower_recursively(petal_number: int, petal_length: float):
    """Draws a flower based on the petal number and petal length
    Includes layers of flower petals depending on the petal number"""
    if petal_number == 4:
        # draw the center of the flower
        t.goto(0, 0)
        t.color(PETAL_COLOURS["sunglow"])
        t.shape("circle")
        t.stamp()
    else:
        # draw more petals
        draw_one_petal(petal_number, petal_length)
        # draw a shorter layer of petals
        draw_flower_recursively(petal_number - 1, petal_length * 0.7)


draw_flower_recursively(11, 200)


# # draw flower with more petals
# def draw_flower_more_petals(petal_number: int, petal_length: float):
#     if petal_number == 0:
#         # draw the center of the flower
#         t.goto(0, 0)
#         t.color("yellow")
#         t.shape("circle")
#         t.stamp()
#     else:
#         # draw the number of petals
#         for _ in range(petal_number):
#             t.color("pink")
#             t.forward(petal_length)
#             t.left(360 / petal_number)
#             t.forward(petal_length)
#             t.left(180 - (360 / petal_number))
#             t.forward(petal_length)
#             t.right(180 - (360 / petal_number))
#             t.backward(petal_length)
#         # draw more petals within petals
#         for _ in range(petal_number):
#             t.color("lightblue")
#             t.goto(0, 0)
#             t.left(360 / petal_number * 2)
#             t.forward(petal_length * 0.7)
#             t.left(360 / petal_number * 2)
#             t.forward(petal_length * 0.7)
#             t.left(180 - (360 / petal_number * 2))
#             t.forward(petal_length * 0.7)
#             t.right(180 - (360 / petal_number * 2))
#             t.backward(petal_length * 0.7)
#         draw_flower_more_petals(0, 0)


# # draw flower without recursion
# def draw_flower(petal_number: int, petal_length: float):
#     if petal_number == 0:
#         # draw the center of the flower
#         t.color("yellow")
#         t.shape("circle")
#         t.stamp()
#     else:
#         # draw the number of petals
#         for _ in range(petal_number):
#             t.forward(petal_length)
#             t.left(360 / petal_number)
#             t.forward(petal_length)
#             t.left(180 - (360 / petal_number))
#             t.forward(petal_length)
#             t.right(180 - (360 / petal_number))
#             t.backward(petal_length)
#         draw_flower(0, 0)


wn.exitonclick()
