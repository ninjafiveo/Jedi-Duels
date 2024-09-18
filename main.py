import random

# Define the Jedi and Sith classes
# Extend these classes by adding methods and attributes as needed

class Jedi:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        # Method to introduce the Jedi
        pass  # Fill this in with functionality

    def lightsaber_attack(self, sith):
        # Method for a lightsaber attack
        pass  # Fill this in with functionality


class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        # Method to introduce the Sith
        pass  # Fill this in with functionality

    def lightsaber_attack(self, jedi):
        # Method for a lightsaber attack
        pass  # Fill this in with functionality


# Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
        # Method for random encounters
        pass  # Fill this in with functionality


# Main adventure loop
def start_adventure():
    print("Welcome to the Star Wars Adventure!")
    player_name = input("Enter your name, traveler: ")
    adventure = Adventure(player_name)

    # Create instances of Jedi and Sith
    jedi = Jedi("Obi-Wan Kenobi", "blue", "Master")
    sith = Sith("Darth Vader", "red", "Lord")

    # Start the adventure loop
    while True:
        print("\nWhat would you like to do?")
        action = input("Explore / Duel / Quit: ").lower()

        if action == "explore":
            encounter = adventure.random_encounter()
            print(encounter)
            # Based on encounter, decide what happens next

        elif action == "duel":
            # Implement dueling functionality here
            print("Prepare for a lightsaber duel!")
            # Example: jedi.lightsaber_attack(sith)

        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

# Start the adventure
start_adventure()
