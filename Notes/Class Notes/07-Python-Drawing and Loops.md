# Drawing and Loops

 14 October 2025

 ## Turtles!

Turtle is a library that helps us visually interact wiith Python code.

To draw on the screen with the turtle library, we need to create turtles first.

 ## Turtle Boilerplate

**Boilerplate** is code that is frequently copied and pasted. It's general use is to set up an environment.

 ```python
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

# TMNT - turtles


wn.exitonclick()
```

## Creating Turtles

> The names of the Teenage Mutant Ninja Turtles:
> Blue bandana - Leonardo (leo)
> Red bandana - Raphael (raph)
> Purple bandana - Donatello (donnie)
> Orange bandana - Michaelangelo (mikey)


To draw on the screen, we need to create **turtle objects**.
To create a turtle, we can do the following:
```python
# create a turtle called mikey

mikey = turtle.Turtle()

```


## Turtle Methods

```python
mikey = turtle.Turtle()  # creates a turtle object

# change attributes
mikey.size()
mikey.color()
mikey.width()
mikey.penup()    # mikey.pu()
mikey.pendown()  # mikey.pd()
mikey.shape()

# actions
mikey.forward()  # mikey.backward()
mikey.left()     # mikey.right()
mikey.circle()
mikey.goto()
```

## Loops / Iteration
**Iternation** is a word that means repetition.

If we ever want to repeat code, we can use a couple of methods.

When we **know how many times** we want to repeat something, we use a `for` loop.

```python
# Print "Hello" 10 times
for _ in range(10):
	print("Hello")

# An example of a loop that uses a `counter`
for counter in range (100):
	print(counter).    # 0, 1, 2, ... ,99
 
```

## Functions and Turtles