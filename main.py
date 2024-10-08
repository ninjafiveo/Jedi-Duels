import random

# Define the Jedi and Sith classes
# Extend these classes by adding methods and attributes as needed

#? Attributes: name, lightsaber_color, rank, and health.
#? Methods:
#? introduce(): Introduce the Jedi.
#? lightsaber_attack(sith): Attack the Sith and reduce their health.
#? use_force(): Use a Force ability.

class Jedi:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"Howdy, I am Jedi {self.name}, a {self.rank}. My lightsaber is {self.lightsaber_color}.")

    def lightsaber_attack(self, sith):
        # Method for a lightsaber attack
        damage = random.randint(10, 30)
        sith.health -= damage
        print(f"{self.name} attacks {sith.name} with {self.lightsaber_color}, dealing {damage} damage!")

        if sith.health <=0:
            print(f"{sith.name} has been defeated.")
        else:
            print(f"{sith.name} has been {sith.health} left..")
    #? Added use_force
    def use_force(self):
        print(f"{self.name} uses the Force to gain and advantage.")
    


class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        # Method to introduce the Sith
        print(f"Howdy, I am Sith Lord {self.name}, a {self.rank}. My lightsaber is {self.lightsaber_color}.")
       

    def lightsaber_attack(self, jedi):
        damage = random.randint(10, 30)
        jedi.health -= damage
        print(f"{self.name} attacks {jedi.name} with {self.lightsaber_color}, dealing {damage} damage!")

        if jedi.health <=0:
            print(f"{jedi.name} has been defeated.")
        else:
            print(f"{jedi.name} has been {jedi.health} left..")


# Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
        # Method for random encounters
        encounters = [
            "You find Jedi Temple",
            "You encountered a Sith Lord!",
            "You find the Millenium Falcon",
            "You found a holocron",
            "You were ambushed by bounty hunters"
        ]
        
        return random.choice(encounters)
        #? How It Works:
        #* A list of possible events (encounters) is defined, such as finding a Jedi temple or encountering a Sith Lord.
        #* The random.choice() function selects one of these events at random and returns it as the result of the method.
        #* The result is then displayed to the player, showing what they encountered during their exploration.


#! Function to handle a duel between Jedi and Sith
#? Duel Function:
#* The start_duel() function handles the dueling between Jedi and Sith. It alternates attacks between the two until one of them is defeated.
#* Purpose: This function simulates a lightsaber duel between a Jedi and a Sith. It handles the back-and-forth attacks between the two characters until one of them is defeated (i.e., their health reaches zero).
def start_duel(jedi, sith):
    print("\nA duel has begun!")
    #? Loop: The while loop continues as long as both the Jedi and Sith have more than 0 health. It will alternate attacks between the two characters until one character’s health is reduced to 0 or below.
    while jedi.health > 0 and sith.health > 0:
        jedi.lightsaber_attack(sith)
        if sith.health > 0:
            sith.lightsaber_attack(jedi)
        if jedi.health <= 0:
            print(f"{jedi.name} has been defeated! The Sith reign supreme.")
        elif sith.health <= 0:
            print(f"{sith.name} has been defeated! The Jedi are victorious.")
        #? How It Works:

        #* Jedi Attacks First: The Jedi attacks the Sith using the lightsaber_attack() method. The method reduces the Sith’s health by a random amount.
        #* Sith Counterattacks (if alive): If the Sith is still alive (i.e., health is above 0), the Sith attacks the Jedi.
        #* Check for Defeat: After each attack, the code checks if either character’s health has dropped to 0 or below.
        #* If the Jedi’s health is 0 or below, the Sith wins, and the message "The Sith reign supreme" is displayed.
        #* If the Sith’s health is 0 or below, the Jedi wins, and the message "The Jedi are victorious" is displayed.

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
            start_duel(jedi, sith) #? Added Start Duel Created Above

        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

# Start the adventure
start_adventure()
