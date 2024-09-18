import random

# Define the Jedi and Sith classes
# Students will extend these classes by adding methods and attributes as needed

class Jedi:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        # Method to introduce the Jedi
        print(f"I am {self.name}, a {self.rank}. my lightsaber is {self.lightsaber_color}.")
    

    def lightsaber_attack(self, sith, name):
        # Method for a lightsaber attack
        sith.health - 50
        print(f"jedi {name} attacks sith! they're now at {sith.health} health.")


class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        # Method to introduce the Sith
        print(f"I am {self.name}, a {self.rank}. my lightsaber is {self.lightsaber_color}.")
        

    def lightsaber_attack(self, jedi, name):
        # Method for a lightsaber attack
        jedi.health - 50
        print(f"sith {name} attacks jedi! they're now at {jedi.health} health.")

# Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
        # Method for random encounters
        encounters = [
            "you found a jedi!",
            "you encountered a sith!",
            "you found a holocron!"
        ]
        return random.choice(encounters)


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
            if "Jedi" in encounter:
                jedi.introduce()
            elif "Sith" in encounter:
                sith.intyroduce()

        elif action == "duel":
            start_duel(jedi, sith)
            print("Prepare for a lightsaber duel!")
            # Example: jedi.lightsaber_attack(sith)

        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

    def start_duel(jedi, sith):
        print ("a duel has started !")
        jedi.lightsaber_attack(sith)
        sith.lightsaber_attack(jedi)
        print(f"jedi {jedi.name} health: {jedi.health}")
        print(f"sith {sith.name} health: {sith.health}")

# Start the adventure
start_adventure()
