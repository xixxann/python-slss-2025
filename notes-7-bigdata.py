# Big Data
# Author: Angel Li
# 17 November 2025

# Open files using Python
# Read the data in the files
# Interpret the data that we read


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    # Print the fist line of the file
    _ = file.readline()

    # # Get information about the fave pizza place
    # uncle_fatihs = 0
    # club_ilia = 0
    # pizza_hut = 0

    # # Get info for fave burritos
    # guadalupe = 0
    # quesada = 0

    # Get info for fave healthy food
    natures_garden = 0
    chopped_leaf = 0
    subway = 0
    veggie_lunch = 0
    steves_pokebar = 0

    for line in file:
        # fave pizza is in column 5 (4th index)
        # a line is a string
        # convert the string to a list
        # split the line wherever a , is
        info = line.split(",")
        # fave_pizza = info[4]
        # fave_burrito = info[5]
        healthy_food = info[-1].lower().strip()

        if healthy_food == "nature's garden":
            natures_garden += 1
        elif healthy_food == "chopped leaf":
            chopped_leaf += 1
        elif healthy_food == "subway":
            subway += 1
        elif healthy_food == "veggie lunch":
            veggie_lunch += 1
        elif healthy_food == "steve's poke bar":
            steves_pokebar += 1

    # # Display Results
    print(f"Nature's Garden: {natures_garden}")
    print(f"Chopped Leaf: {chopped_leaf}")
    print(f"Subway: {subway}")
    print(f"Veggie Lunch: {veggie_lunch}")
    print(f"Steve's Poke Bar: {steves_pokebar}")

    #     if fave_pizza == "Uncle Fatih's":
    #         uncle_fatihs += 1
    #     elif fave_pizza == "Club Ilia":
    #         club_ilia += 1
    #     elif fave_pizza == "Pizza Hut":
    #         pizza_hut += 1

    #     if fave_burrito == "Guadalupe (MBC)":
    #         guadalupe += 1
    #     elif fave_burrito == "Quesada (Cornerstone)":
    #         quesada += 1

    # if guadalupe > quesada:
    #     print("Guadalupe is the most popular burrito place!")
    # elif quesada > guadalupe:
    #     print("Quesada is the most popular burrito place!")
    # else:
    #     print("It's a tie between Guadalupe and Quesada!")

    # # Display results
    # print(f"Uncle Fatih's Votes: {uncle_fatihs}")
    # print(f"Club Ilia's Votes: {club_ilia}")
    # print(f"Pizza Hut's Votes: {pizza_hut}")

    file.close()


if __name__ == "__main__":
    main()
