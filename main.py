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
        print(f"Howdy, I am Jedi {self.name}, a {self.rank}. My lightsaber is{self.lightsaber_color}")
        

    def lightsaber_attack(self, sith):
        damage = random.randint(10,30)
        sith.health -= damage
        print(f"{self.name} attacks {sith.name} {self.lightsaber_color} dealing {damage} damage.")
        if sith.health <= 0:
            print(f"{sith.name} has been defeated.")
        else:
            print(f"{sith.name} has been hit {sith.health} and left.")

    def use_force(self):
        print(f"{self.name} uses The Force to gain an advantage.")



class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"I am Sith Lord {self.name}")
        

    def lightsaber_attack(self, jedi):
        damage = random.randint(10,30)
        jedi.health -= damage
        print(f"{self.name} attacks {jedi.name} {self.lightsaber_color} dealing {damage} damage.")
        if jedi.health <= 0:
            print(f"{jedi.name} has been defeated.")
        else:
            print(f"{jedi.name} has been {jedi.health} left.")
        
    def use_force(self):
        print(f"{self.name} uses The Force to gain an advantage.")

         # Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
        encounters = [
            "You find a Jedi temple",
            "You encountered a Sith Lord", 
            "You have found the Millenium Falcon"
            "You have found the holocron", 
            "You were ambuhed by bounty hunters"
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
            # Based on encounter, students will decide what happens next

        elif action == "duel":
            # Students will implement dueling functionality here
            print("Prepare for a lightsaber duel!")
            # Example: jedi.lightsaber_attack(sith)
            start_duel(jedi, sith)

        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

# start duel
def start_duel(jedi, sith):
    print("A duel has begun")
    while jedi.health > 0 and sith.health > 0:
        jedi.lightsaber_attack(sith)
        sith.lightsaber_attack(jedi)
        if sith.health > 0:
            jedi.lightsaber_attack(sith)
            print(f"Sith has {sith.health}")
        if jedi.health > 0:
            sith.lightsaber_attack(jedi)
            print(f"Jedi has {jedi.health}")
        

# Start the adventure
start_adventure()

