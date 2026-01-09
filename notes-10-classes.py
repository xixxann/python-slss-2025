# Classes and Objects
# Author: Angel Li
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        # Initialize the propertes of Pokemon
        self.name = ""
        self.species = ""
        self.type = "normal"
        self.move = "Running man"
        self.shiny = False
        self.age = 0
        self.level = 1
        print("A pokemon is born!")
        # One out of 4096 should be shiny
        if random.randint(0, 4096):
            self.shiny = False
        else:
            self.shiny = True
            print(f"{self.name} is shiny!")

    def talk(self):
        """Hear what the pokemon has to say.
        The pokemon says it species name."""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        """Display the stats of the Pokemon"""
        print(f"---{self.species}------")
        print(f"  Name: {self.name}")
        print(f"  Type: {self.type}")
        print(f"  Age: {self.age}")
        print(f"  Level: {self.level}")
        print("-----------------")

    def dance(self):
        """Tell the pokemon to dance."""
        print(f"{self.name} does the {self.move} dance!")


class Squirtle(Pokemon):
    def __init__(self):
        # Call the superclass constructor explicity
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"
        self.has_sunglasses = True

    def water_gun(self):
        """Use the water gun attack."""
        print(f"{self.name} used water gun.")
        # TODO: check to see if it's effective


class Ditto(Pokemon):
    def __init__(self):
        # Call the superclass constructor explicity
        super().__init__()
        self.name = "Ditto"
        self.species = "Ditto"
        self.type = "water"
        self.has_sunglasses = True

    def duplicate(self):
        """Duplicates itself a different times"""
        print(f"{self.name} duplicates itself {random.randint(0, 100)} times.")

    def clone(self):
        """Clones itself into something else."""
        object = input("What do you want ditto to clone into? ")
        print(f"{self.name} clones itself into {object}!")


class Mew(Pokemon):
    def __init__(self):
        # Constructor
        super().__init__()
        self.name = "Mew"
        self.type = "psychic"
        self.species = "Mew"
        self.level = 1
        self.age = 0


if __name__ == "__main__":
    # Create a pokemon object
    pokemon_one = Pokemon()
    # View its properties
    print("Pokemon Name: ", pokemon_one.name)
    # Change some of its properties
    pokemon_one.name = "Gary"
    print("Pokemon Name: ", pokemon_one.name)
    # Create another pokemon object
    pokemon_two = Pokemon()
    print("Pokemon two's name:", pokemon_two.name)
    # Compare the two pokemon
    if pokemon_one == pokemon_two:
        print("These are the same pokemon?")
    else:
        print("They're individual, distinct pokemon")
    # Check if both objects are pokemon
    if type(pokemon_one) is Pokemon:  # 'is' checks type
        print(f"{pokemon_one.name} is a Pokemon.")
    if type(pokemon_two) is Pokemon:
        print(f"{pokemon_two.name} is a Pokemon.")

    # Have Gary talk
    pokemon_one.talk()
    pokemon_two.talk()
    pokemon_one.stats()
    pokemon_two.stats()
    # Have Gary dance
    pokemon_one.dance()

    squirtle_one = Squirtle()
    squirtle_one.talk()
    squirtle_one.water_gun()

    ditto_one = Ditto()
    ditto_one.talk()
    ditto_one.clone()
    ditto_one.duplicate()

    pokemon_three = Mew()
    pokemon_three.talk()
    pokemon_three.stats()
