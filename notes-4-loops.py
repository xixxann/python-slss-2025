# Drawing and Loops
# Author: Angel Li
# 14 October 2025


import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightblue")

# TMNT - turtles
mikey = turtle.Turtle()
# mikey.turtlesize(5)  # size
mikey.color("darkgreen")  # colour

# # draw snowman
# mikey.shape("turtle")
# mikey.speed(2)
# mikey.penup()
# mikey.goto(-300, -300)  # return to spot on the coordinate
# mikey.pendown()
# mikey.width(10)
# mikey.pencolor("darkblue")
# mikey.circle(100)
# mikey.penup()
# mikey.goto(-300, -100)
# mikey.pendown()
# mikey.circle(60)
# mikey.penup()
# mikey.goto(-300, 20)
# mikey.pendown()
# mikey.circle(40)
# mikey.penup()
# mikey.goto(-290, 50)
# mikey.pendown()
# mikey.circle(2)
# mikey.penup()
# mikey.goto(-310, 50)
# mikey.pendown()
# mikey.circle(2)

# # draw house
# mikey.penup()
# mikey.goto(0, 150)
# mikey.pendown()
# mikey.pencolor("blue")
# mikey.speed(2)
# mikey.width(10)
# mikey.forward(500)
# mikey.right(90)
# mikey.forward(500)
# mikey.right(90)
# mikey.forward(500)
# mikey.right(90)
# mikey.forward(500)
# mikey.penup()
# mikey.right(45)
# mikey.pendown()
# mikey.forward(350)
# mikey.right(90)
# mikey.forward(350)

# # draw the door
# mikey.penup()
# mikey.right(45)
# mikey.forward(500)
# mikey.right(90)
# mikey.forward(200)
# mikey.pendown()
# mikey.right(90)
# mikey.pendown()
# mikey.pencolor("purple")
# mikey.forward(200)
# mikey.left(90)
# mikey.forward(100)
# mikey.left(90)
# mikey.forward(200)
# mikey.hideturtle()


# Create a fn that makes a cookie
# at (x.y)
def make_cookie(x: int, y: int):
    # Make sure that turtle is pointing east
    mikey.setheading(0)
    # Change the cookie colour
    mikey.color("brown")
    # Draw a circle
    mikey.pu()
    mikey.goto(-5 + x, -30 + y)
    mikey.pd()
    mikey.circle(30)
    # Put a chocolate chip on the top left side
    mikey.pu()
    mikey.goto(-10 + x, 10 + y)
    mikey.stamp()
    # Chocolate chip on the top right
    mikey.goto(10 + x, 10 + y)
    mikey.stamp()
    # Chocolate chip on the bottom right
    mikey.goto(10 + x, -10 + y)
    mikey.stamp()
    # Chocolate chip on the bottom left
    mikey.goto(-10 + x, -10 + y)
    mikey.stamp()
    # Chocolate chip in the middle
    mikey.goto(0 + x, 0 + y)
    mikey.stamp()


mikey.speed(0)
# Make cookies in an x
for counter in range(50):
    counter = counter * 50
    make_cookie(counter, counter)
    make_cookie(counter, -counter)
    make_cookie(-counter, -counter)
    make_cookie(-counter, counter)

window.exitonclick()
