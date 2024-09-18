import random

# Define the Jedi class
#! Jedi Class:

#? Attributes: name, lightsaber_color, rank, health (default 100).
#? Methods:
#* introduce(): Prints a message introducing the Jedi, including their name, lightsaber color, and rank.
#* lightsaber_attack(sith): The Jedi attacks a Sith, dealing random damage between 10 and 30 points, and reduces the Sith’s health. If the Sith’s health drops to or below 0, the Sith is defeated.
#* use_force(): This method simulates the Jedi using the Force, though it's not directly tied to combat.
class Jedi:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"I am Jedi {self.name}, a {self.rank}. My lightsaber is {self.lightsaber_color}.")

    def lightsaber_attack(self, sith):
        damage = random.randint(10, 30)
        sith.health -= damage
        print(f"{self.name} attacks {sith.name} with a {self.lightsaber_color} lightsaber, dealing {damage} damage!")
        if sith.health <= 0:
            print(f"{sith.name} has been defeated!")
        else:
            print(f"{sith.name} has {sith.health} health remaining.")

    def use_force(self):
        print(f"{self.name} uses the Force to gain an advantage!")

#! Define the Sith class
#? Attributes: name, lightsaber_color, rank, health (default 100).
#? Methods:
#* introduce(): Prints a message introducing the Sith, including their name, lightsaber color, and rank.
#* lightsaber_attack(jedi): The Sith attacks a Jedi, dealing random damage between 10 and 30 points, and reduces the Jedi’s health. If the Jedi’s health drops to or below 0, the Jedi is defeated.
#* use_force(): Similar to the Jedi's ability, this simulates the Sith using the Dark Side of the Force.
class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"I am Sith {self.name}, a {self.rank}. My lightsaber is {self.lightsaber_color}.")

    def lightsaber_attack(self, jedi):
        damage = random.randint(10, 30)
        jedi.health -= damage
        print(f"{self.name} attacks {jedi.name} with a {self.lightsaber_color} lightsaber, dealing {damage} damage!")
        if jedi.health <= 0:
            print(f"{jedi.name} has been defeated!")
        else:
            print(f"{jedi.name} has {jedi.health} health remaining.")

    def use_force(self):
        print(f"{self.name} uses the Dark Side of the Force to gain an advantage!")

#! Define the Adventure class for random encounters
#? Method: random_encounter() generates a random event (such as finding a Jedi temple or encountering a Sith Lord) when the player explores the galaxy.
#* Purpose: The Adventure class manages the player’s exploration in the game. It stores the player’s name and provides the method for generating random events while exploring the galaxy.
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name
    #* Purpose: The constructor method (__init__) initializes an Adventure object when a player starts the game. It stores the player’s name in the self.player_name attribute, so we can reference the player’s name later if needed.

    def random_encounter(self):
    #* Purpose: The constructor method (__init__) initializes an Adventure object when a player starts the game. It stores the player’s name in the self.player_name attribute, so we can reference the player’s name later if needed.
        encounters = [
            "You found a Jedi temple!",
            "You encountered a Sith Lord!",
            "You found a holocron!",
            "You were ambushed by bounty hunters!"
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
#? The main loop allows the player to choose between exploring, dueling, or quitting the game. If they explore, a random encounter is generated. If they choose to duel, the Jedi and Sith battle until one is victorious.
#* Purpose: This function is the main loop of the game. It allows the player to explore the galaxy, duel with a Sith, or quit the game. It repeatedly prompts the player for an action until they decide to quit.
def start_adventure():
    print("Welcome to the Star Wars Adventure!")
    player_name = input("Enter your name, traveler: ") #Player Name: The player is prompted to enter their name, which is passed to the Adventure class to track the player throughout the game.
    adventure = Adventure(player_name)

    #! Create instances of Jedi and Sith
    #? Two characters, jedi (Obi-Wan Kenobi) and sith (Darth Vader), are created as instances of their respective classes. These characters will be used in the game for duels and interactions.
    jedi = Jedi("Obi-Wan Kenobi", "blue", "Master")
    sith = Sith("Darth Vader", "red", "Lord")

    #!  Main Loop
    #*     The while True loop continuously prompts the player to choose one of three actions:
    #* Explore: If the player chooses to explore, the game calls the random_encounter() method from the Adventure class to generate a random event. Depending on the encounter, the Jedi or Sith will introduce themselves.
    #* Duel: If the player chooses to duel, the start_duel() function is called, and the Jedi and Sith battle until one of them is defeated.
    #* Quit: If the player chooses to quit, the game ends by breaking the loop and printing a farewell message ("May the Force be with you").
    while True:
        print("\nWhat would you like to do?")
        action = input("Explore / Duel / Quit: ").lower()

        if action == "explore":
            encounter = adventure.random_encounter()
            print(f"{player_name} explores the galaxy and: {encounter}")
            if "Jedi" in encounter:
                jedi.introduce()
            elif "Sith" in encounter:
                sith.introduce()

        elif action == "duel":
            start_duel(jedi, sith)

        elif action == "quit":
            print("May the Force be with you. Goodbye!")
            break

        else:
            print("Invalid action, try again.")
            #?  Handling Invalid Inputs:
            #* If the player inputs an invalid action (i.e., not "explore", "duel", or "quit"), the game prints an error message and prompts the player again for input.

# Start the adventure
if __name__ == "__main__":
    start_adventure()
