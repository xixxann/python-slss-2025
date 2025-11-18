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
    header_row = file.readline()

    # Get information about the fave pizza place
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0

    for line in file:
        # fave pizza is in column 5 (4th index)
        # a line is a string
        # convert the string to a list
        # split the line wherever a , is
        info = line.split(",")
        fave_pizza = info[4]

        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fave_pizza == "Club Ilia":
            club_ilia += 1
        elif fave_pizza == "Pizza Hut":
            pizza_hut += 1

    # Display results
    print(f"Uncle Fatih's Votes: {uncle_fatihs}")
    print(f"Club Ilia's Votes: {club_ilia}")
    print(f"Pizza Hut's Votes: {pizza_hut}")

    file.close()


if __name__ == "__main__":
    main()
