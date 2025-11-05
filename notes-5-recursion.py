# Recursion
# Author: Angel Li
# 20 October


# We're drawing trees (recursively)

import turtle

# Create a turtle that draws
wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()


def draw_asymmetric_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color("pink")
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_asymmetric_tree(level - 1, branch_length * 0.5)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_asymmetric_tree(level - 1, branch_length * 0.9)
        if level <= 2:
            t.left(37)
            draw_asymmetric_tree(level - 1, branch_length * 0.7)
            t.backward(branch_length)
        elif level > 2:
            t.right(30)
            draw_asymmetric_tree(level - 1, branch_length * 0.3)


# Dictionary to hold colours
LEAF_COLOURS = {
    "spring": "#ffc0be",
    "summer": "#c5d86d",
    "fall": "#ba1200",
    "winter": "#e3f2fd",
}


def draw_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color(LEAF_COLOURS["summer"])
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(37)  # point north
        t.backward(branch_length)


def draw_complicated_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color("red")
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(37)  # point north
        # 5. Go straight
        draw_complicated_tree(level - 1, branch_length * 0.8)
        t.backward(branch_length)


# Set up the turtle
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()


draw_tree(2, 128)
wn.exitonclick()


# Factorials
def factorial(num: int) -> int:
    """Returns the factorial of a given number calculated recursively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


# print(factorial(4))


# def fibonacci(num: int) -> int:
#     """Returns the nth fibonacci number and calculate recursively"""
#     # if the number is greater than 2
#     # return fibonacci(num - 1) + fibonacci(num - 2)
#     # else
#     # return 1
