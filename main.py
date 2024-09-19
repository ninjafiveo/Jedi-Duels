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
         print(f"howdy, I am Jedi {self.name}, a {self.rank}. My Lightsaber is {self.lightsaber_color}")

    def lightsaber_attack(self, sith):
        # Method to introduce the Jedi
        damage = random.randint(10, 30)
        sith.health -= damage
        print(f"{self.name} attacks {sith.name} with {self.lightsaber_color}, dealing {damage} damage")
        if sith.health <= 0:
            print(f"{sith.name} has been defeated")
        else:
            print(f"{sith.name} has {sith.health} left...")

    def use_force(self, ):
        print(f"{self.name} uses the force to gain and advantage.")


class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        # Method to introduce the Sith
        print(f"howdy, I am Sith Lord {self.name}, a {self.rank}. My Lightsaber is {self.lightsaber_color}")

    def lightsaber_attack(self, jedi):
         # Method to introduce the Jedi
        damage = random.randint(10, 30)
        jedi.health -= damage
        print(f"{self.name} attacks {jedi.name} with {self.lightsaber_color}, dealing {damage} damage")
        if jedi.health <= 0:
            print(f"{jedi.name} has been defeated")
        else:
            print(f"{jedi.name} has {jedi.health} left...")

    def use_force(self, ):
        print(f"{self.name} uses the force to gain and advantage.")


# Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
        # Method for random encounters
        encounters = [
            "you find a jedi temple",
            "you encountered a Sith Lord",
            "You Find the Millenium falcon",
            "you found a holocron",
            "you were ambushed by bounty hunters"
        ]
        return random.choice(encounters)

def start_duel(jedi, sith):
while jedi.health

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
            start_duel(jedi, sith)

        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

# Start the adventure
start_adventure()