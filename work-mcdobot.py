# Work - McDoBot
# Author: Angel Li
# 6 October

# It should accept  Yes/yes  or  No/no
# as inputs, and reply appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer and say that it does not understand.

want_fries = input("Do you want fries with your meal? ")

if want_fries.lower().strip("!.,?") == "yes":
    print("Here is your meal with fries!")
elif want_fries.lower().strip("!.,?") == "no":
    print("Here is your meal without fries!")
else:
    print(f"Sorry, I don't understand what {want_fries} means.")
