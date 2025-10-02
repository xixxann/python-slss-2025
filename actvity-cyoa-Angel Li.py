# Choose Your Own Adventure
# Angel Li
# 24 September

# Choose your own adventure story focusing on using variables and branching/conditionals.

import time

print("You open your eyes and you realized that you are in a forest.")
time.sleep(1.0)

print("In front of you, there is a green fairy.")
time.sleep(1.0)

user_name = input("Hello there, what's your name? ")
time.sleep(1.0)

print(f"It's nice to meet you, {user_name}.")
time.sleep(1.5)

print(
    "Unfortunately, you somehow landed into the Wilderdeep, a forest away from your world."
)
time.sleep(1.5)

fairy_help = input(
    "But I can help you escape this world, do you want my help? (TYPE yes or no) "
)

if fairy_help == "yes":
    print("Alright, let's keep walking then.")
elif fairy_help == "no":
    print("Fine then, go figure it out yourself.")
time.sleep(1.5)

if fairy_help == "no":
    print("You turn down the fairy's offer, brushing off her warning as superstition.")
    time.sleep(2)
    print(
        "As you continue to walk down the path, you felt something digging deep into the your left ankle."
    )
    time.sleep(2)
    print("You look down and find out that it was a poisonous snake.")
    time.sleep(2)
    print("YOU HAVE DIED.")
    continue_game = False

if fairy_help == "yes":
    print(
        "As you continue to walk, the fairy tells you that there is an observer in the forest that can control who can escape and who stays in the forest."
    )
    time.sleep(3)
    print(
        "However, she assures you that as long as you get through the obstacles the observer give you, you are guaranteed to survive."
    )
    time.sleep(2.5)
    print(
        "After a long tiring hour of walking through the thick bushes and passing under tree tops, you happen to find three differently coloured mushrooms."
    )
    time.sleep(3)
    print(
        "The fairy tells you that this is one of the challenges and you must eat one of the three mushrooms."
    )
    time.sleep(3)
    print(
        "She tells you that there one of them will cause death, the other will acquire a tool, and the remaining one will give you a trivia."
    )
    time.sleep(3)
    mushroom_colour = input(
        "Now, which mushroom should you choose? (Type red, blue, or purple) "
    )
    if mushroom_colour == "red":
        print("You bite into the mushroom, expecting a bitter taste...")
        time.sleep(1.5)
        print("But it's strangely sweet.")
        time.sleep(1.5)
        print(
            "With a sudeen flash of light, a glowing sword materializes in front of you, hovering in the air, humming with ancient energy."
        )
        time.sleep(1.5)
        print("YOU HAVE OBTAINED A SWORD!")
        time.sleep(1.5)
        obtained_sword = True
        if obtained_sword:
            print(
                "With your new weapon, you set off once more, the forest stretching endlessly ahead."
            )
            time.sleep(2)
            print(
                "By the time night falls, the woods are cloaked in darkness, broken only by sivers of moonlight."
            )
            time.sleep(2)
            print(
                "Suddenly, a bear steps into your path, eyes glowing in the moonlight. It growls at you."
            )
            time.sleep(2)
            continue_game = True
            if continue_game:
                bear_choice = input(
                    "What should you do? (TYPE run away or fight back) "
                )
                if bear_choice == "run away":
                    print(f"Well, to {bear_choice} is a good idea.")
                    time.sleep(1.5)
                    print("You turn and sprint into the trees, heart pounding.")
                    time.sleep(1.5)
                    print("But the bear is faster.")
                    time.sleep(1.5)
                    print("With a roar, it swipes and its claws grazed your back.")
                    time.sleep(1.5)
                    print("Pain burns, but you don't stop.")
                    time.sleep(1.5)
                    print("You dive behind a fallen log, gasping for breath.")
                    time.sleep(1.5)
                    print("You're wounded, but alive...for now")
                    time.sleep(1.5)
                    fight_choice = input(
                        "Will you fight back or continue to run away? (TYPE fight back or run away) "
                    )
                    if fight_choice == "fight back":
                        print("You raise your sword, wounded but determined.")
                        time.sleep(1.5)
                        print("As the bear charges, you strike with all your strength.")
                        time.sleep(1.5)
                        print("After a fierce clash, the beast falls.")
                        time.sleep(1.5)
                        print(
                            "As it takes its final breath, its form behind to shimmer."
                        )
                        time.sleep(1.5)
                        print(
                            "The fur fades, revealing glowing runes beneath. This was no ordinary bear..."
                        )
                        time.sleep(1.5)
                        print("It was the Observer of the Forest!")
                        time.sleep(1.5)
                        print("The fairy says: 'You made it!'")
                        time.sleep(1.5)
                        print(
                            "A portal opens before you, swirling with light. Without hesitation, you step through..."
                        )
                        time.sleep(1.5)
                        print("and land safely back in your home.")
                        time.sleep(1.5)
                        print("YOU HAVE SURVIVED!")
                    elif fight_choice == "run away":
                        print(
                            "You sprint deeper into the shadows, desperate to escape the pain in your back."
                        )
                        time.sleep(1.5)
                        print("But the bear's growls echo closer and closer.")
                        time.sleep(1.5)
                        print("Your legs fater, your strength giving out.")
                        time.sleep(1.5)
                        print("Before you can react, the beast is upon you.")
                        time.sleep(1.5)
                        print("Darkness swallows you whole.")
                        time.sleep(1.5)
                        print("YOU HAVE DIED.")
                elif bear_choice == "fight back":
                    print("You build up your confidence and raise your sword.")
                    time.sleep(1.5)
                    print("As the bear charges, you strike with all your strength.")
                    time.sleep(1.5)
                    print("After a fierce clash, the beast falls.")
                    time.sleep(1.5)
                    print(
                        "As it takes its final breath, its fur fades, revealing glowing runes beneath."
                    )
                    time.sleep(1.5)
                    print("This was no ordinary bear...")
                    time.sleep(1.5)
                    print("It was the Observer of the Forest!")
                    time.sleep(1.5)
                    print("The fairy says: 'You escaped from the forest!'")
                    time.sleep(1.5)
                    print(
                        "A portal opens before you, swirling with light. Without hesitation, you step through..."
                    )
                    time.sleep(1.5)
                    print("and land safely back in your home.")
                    time.sleep(1.5)
                    print("YOU HAVE SURVIVED!")
                else:
                    print("You made the wrong choice.")
                    time.sleep(1.0)
                    print("YOU HAVE DIED.")
    elif mushroom_colour == "blue":
        print(
            "You take a bite of the strange blue mushroom, hoping this is the right answer."
        )
        time.sleep(1.5)
        print(
            "Within moments, your vision blurs, your knees buckle, and the world fades to black..."
        )
        time.sleep(2)
        print("YOU HAVE DIED.")
        time.sleep(1.5)
        print("Perhaps next time, a little caution would serve you well.")
        obtained_sword = False
    elif mushroom_colour == "purple":
        print("You bite into the mushroom.")
        time.sleep(1.0)
        print(
            "The world shimmers for a moment...and suddenly, a glowing question floats in the air before you."
        )
        time.sleep(1.5)
        print(
            "A voice whispers: Answer me this, brave human...one wrong word and you shall die"
        )
        time.sleep(1.5)
        trivia_question = input(
            "What bird is traditonally considered a symbol for wisdom? (TYPE owl or raven) "
        )
        if trivia_question == "owl":
            print("You are correct!")
            time.sleep(1.0)
            print(
                "A soft glow surrounds you, and in your hand, a sword materializes from thin air."
            )
            time.sleep(1.5)
            print("YOU HAVE OBTAINED A SWORD!")
            time.sleep(1.5)
            obtained_sword = True
            if obtained_sword:
                print(
                    "With your new weapon, you set off once more, the forest stretching endlessly ahead."
                )
                time.sleep(2)
                print(
                    "By the time night falls, the woods are cloaked in darkness, broken only by sivers of moonlight."
                )
                time.sleep(2)
                print(
                    "Suddenly, a bear steps into your path, eyes glowing in the moonlight. It growls at you."
                )
                time.sleep(2)
                continue_game = True
                if continue_game:
                    bear_choice = input(
                        "What should you do? (TYPE run away or fight back) "
                    )
                    if bear_choice == "run away":
                        print(f"Well, to {bear_choice} is a good idea.")
                        time.sleep(1.5)
                        print("You turn and sprint into the trees, heart pounding.")
                        time.sleep(1.5)
                        print("But the bear is faster.")
                        time.sleep(1.5)
                        print("With a roar, it swipes and its claws grazed your back.")
                        time.sleep(1.5)
                        print("Pain burns, but you don't stop.")
                        time.sleep(1.5)
                        print("You dive behind a fallen log, gasping for breath.")
                        time.sleep(1.5)
                        print("You're wounded, but alive...for now")
                        time.sleep(1.5)
                        fight_choice = input(
                            "Will you fight back or continue to run away? (TYPE fight back or run away) "
                        )
                        if fight_choice == "fight back":
                            print("You raise your sword, wounded but determined.")
                            time.sleep(1.5)
                            print(
                                "As the bear charges, you strike with all your strength."
                            )
                            time.sleep(1.5)
                            print("After a fierce clash, the beast falls.")
                            time.sleep(1.5)
                            print(
                                "As it takes its final breath, its form behind to shimmer."
                            )
                            time.sleep(1.5)
                            print(
                                "The fur fades, revealing glowing runes beneath. This was no ordinary bear..."
                            )
                            time.sleep(1.5)
                            print("It was the Observer of the Forest!")
                            time.sleep(1.5)
                            print("The fairy says: 'You made it!'")
                            time.sleep(1.5)
                            print(
                                "A portal opens before you, swirling with light. Without hesitation, you step through..."
                            )
                            time.sleep(1.5)
                            print("and land safely back in your home.")
                            time.sleep(1.5)
                            print("YOU HAVE SURVIVED!")
                        elif fight_choice == "run away":
                            print(
                                "You sprint deeper into the shadows, desperate to escape the pain in your back."
                            )
                            time.sleep(1.5)
                            print("But the bear's growls echo closer and closer.")
                            time.sleep(1.5)
                            print("Your legs fater, your strength giving out.")
                            time.sleep(1.5)
                            print("Before you can react, the beast is upon you.")
                            time.sleep(1.5)
                            print("Darkness swallows you whole.")
                            time.sleep(1.5)
                            print("YOU HAVE DIED.")
                    elif bear_choice == "fight back":
                        print("You build up your confidence and raise your sword.")
                        time.sleep(1.5)
                        print("As the bear charges, you strike with all your strength.")
                        time.sleep(1.5)
                        print("After a fierce clash, the beast falls.")
                        time.sleep(1.5)
                        print(
                            "As it takes its final breath, its fur fades, revealing glowing runes beneath."
                        )
                        time.sleep(1.5)
                        print("This was no ordinary bear...")
                        time.sleep(1.5)
                        print("It was the Observer of the Forest!")
                        time.sleep(1.5)
                        print("The fairy says: 'You escaped from the forest!'")
                        time.sleep(1.5)
                        print(
                            "A portal opens before you, swirling with light. Without hesitation, you step through..."
                        )
                        time.sleep(1.5)
                        print("and land safely back in your home.")
                        time.sleep(1.5)
                        print("YOU HAVE SURVIVED!")
                    else:
                        print("You made the wrong choice.")
                        time.sleep(1.0)
                        print("YOU HAVE DIED.")
        if trivia_question == "raven":
            print("Incorrect.")
            time.sleep(1.5)
            print(
                "The world around you cracks like glass, and you're swallowed by darkness"
            )
            time.sleep(1.5)
            print("YOU HAVE DIED.")
