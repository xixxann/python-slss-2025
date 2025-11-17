# Maths Problems
# Author: Angel Li
# 14 November 2025

# Solving Maths Problems


def main():
    # Question 1: Age in 2049
    current_age = int(input("What is your current age? ").strip(",.?!"))
    # Difference between this year and 2049
    difference = 2049 - 2025
    # Add the difference to current_age
    future_age = difference + current_age
    print(f"In 2049 you will be {future_age} years old!")

    # Question 2: Olympic Judging
    # Tell the user what to do
    print("This is an Olympic Judging. Please give out your scores from 0-10.")
    # Get the judges' scores
    judge_score1 = float(input("Judge 1: "))
    judge_score2 = float(input("Judge 2: "))
    judge_score3 = float(input("Judge 3: "))
    judge_score4 = float(input("Judge 4: "))
    judge_score5 = float(input("Judge 5: "))
    # Calculate the final average score
    average_score = (
        judge_score1 + judge_score2 + judge_score3 + judge_score4 + judge_score5
    ) / 5
    print(f"Your average Olympic score is {average_score}.")

    # Question 3: McDoland's program
    # Ask user if they want fries and burger
    want_burger = str(
        input("Would you like a burger for $5? (Yes/No)").lower().strip(",.?!")
    )
    want_fries = str(
        input("Would you like fries for $3? (Yes/No)").lower().strip(",.?!")
    )

    # Get the total cost
    subtotal = 0

    if want_burger == "yes":
        subtotal = subtotal + 5
    elif want_burger == "no":
        subtotal = subtotal + 0
    else:
        print(" ")

    if want_fries == "yes":
        subtotal = subtotal + 3
    elif want_fries == "no":
        subtotal = subtotal + 0
    else:
        print(" ")

    # Find the tax $$
    tax = subtotal * 0.14
    # Add tax and total together
    final_total = tax + subtotal
    print(f"Your total is ${final_total}.")


if __name__ == "__main__":
    main()
