# Numbers and Operations
# Author: Angel Li
# 5 November 2025

# Work with numbers and operations

# Create an algorithm to gather data to find the most popular bubble tea place around us

import os

NUM_VOTERS = 5


# Version 1
def vote_listed_choices():
    """Display all choices
    5 Users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. CoCo",
        "F. Fresh T",
    ]

    # buckets to hold all votes
    blenz = 0
    bubble_queen = 0
    sun_tea = 0
    heytea = 0
    coco = 0
    fresh_t = 0
    spoiled_votes = 0

    for _ in range(NUM_VOTERS):
        # Clear screen
        os.system("clear")
        # Show all the choices
        print("Vote for your favourte from the list.")
        print("Give the letter of your choice.")
        for choice in CHOICES:
            print(choice)

        # Ask the user for their choice
        vote = input().strip(".,?! ").lower()
        # Keep track of a tally
        if vote == "a":
            blenz = blenz + 1
        elif vote == "b":
            bubble_queen += 1
        elif vote == "c":
            sun_tea += 1
        elif vote == "d":
            heytea += 1
        elif vote == "e":
            coco += 1
        elif vote == "f":
            fresh_t += 1
        else:
            spoiled_votes += 1

    # Data analysis
    # Give the raw scores
    print("Voting Results ---")
    print(f"Blenz: {blenz} votes")
    print(f"Bubble Queen: {bubble_queen} votes")
    print(f"Sun Tea: {sun_tea} votes")
    print(f"HeyTea: {heytea} votes")
    print(f"CoCo: {coco} votes")
    print(f"Fresh T: {fresh_t} votes")
    print(f"Spoiled votes: {spoiled_votes} votes")
    # Give scores as a percentage
    print("Vote share percentage ---")
    total = blenz + bubble_queen + sun_tea + heytea + coco + fresh_t + spoiled_votes
    print("Voting Results ---")
    print(f"Blenz: {blenz / total * 100} %")
    print(f"Bubble Queen: {bubble_queen / total * 100} %")
    print(f"Sun Tea: {sun_tea / total * 100} %")
    print(f"HeyTea: {heytea / total * 100} %")
    print(f"CoCo: {coco / total * 100} %")
    print(f"Fresh T: {fresh_t / total * 100} %")
    print(f"Spoiled votes: {spoiled_votes / total * 100} votes")


# Version 2
def vote_open_choice():
    """Keeps track dynamically of user's choice.
    Note: choices must match text exactly (case is not sensitive)"""

    votes = {}  # holds vote information    key     -> value
    #                           place   -> num votes

    for _ in range(NUM_VOTERS):
        # Ask the user what their fave
        os.system("clear")
        cur_vote = (
            input("What's your favourite local bubble tea cafe? ")
            .lower()
            .strip(",.?! ")
        )

        # Checks if current place is in the votes dictionary
        # If it doesn't exist, initialize the key-value pair
        if cur_vote not in votes:
            votes[cur_vote] = 1
        else:
            votes[cur_vote] += 1

    # Print the results
    print("-------------------------------------")
    print("Results:")

    # By default, iterating over a dictionary gives you the keys
    for place in votes:
        # Print the raw score and percentage for each key in the dictionary
        percentage = votes[place] / NUM_VOTERS * 100

        print(
            f"{place.capitalize()} votes: {votes[place]} | percentage: {percentage}% of the vote"
        )

    print("-------------------------------------")


# Ask the user to give their favourite bubble tea pplace
# Keep track of a tally
# Data analysis
# Give the raw scores
# Give scores as a percentage


def chip_rater():
    """Help gather data about chip crispness
    and quality."""
    questions = [
        "How crispy is the chip out of 5? 0 is mushy, 5 is super crisp.",
        "How would you rate the taste out of 5? 0 is unplatable, 5 is gourmet.",
        "How fresh would you rate the chip out of 5? 0 is stale, 5 is pristine.",
    ]

    # Bucket to hold total ratings
    total_ratings = 0

    # Gve the test subject instructions
    print("Take one chip from the bag.")
    print("Eat is mindfully.")
    print("Give your rating.")

    # Ask questions to the subject
    for question in questions:
        print(question)
        # for each question
        # get their rating for that question
        # out of five
        rating = int(input().strip(",.?!"))

        total_ratings += rating

    # Print out the average rating out of five
    average = total_ratings / len(questions)
    # len(questions) to change the number of values

    print(f"The average rating is {average} *s")


def main():
    # vote_listed_choices()
    # chip_rater()
    vote_open_choice()


if __name__ == "__main__":
    main()
