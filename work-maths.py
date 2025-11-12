# Maths Stuff with Python
# Author: Angel Li
# 12 November 2025


# Machines are good at crunching numbers -
# faster and more accurately than most humans!
# Create a small program that calculates something useful to you (making you smile is useful).
# It should take user input, and use at least one of the number operators
# we saw in class: + / * -. You may modify one of your previous exercises
# to include calculations, if you wish.


def main():
    print("What is the slope of these two lines?")
    y1 = int(input("Y value for the first point: "))
    x1 = int(input("X value for the first point: "))
    y2 = int(input("Y value for the second point: "))
    x2 = int(input("X value for the second point: "))
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope is {slope}!")


if __name__ == "__main__":
    main()
