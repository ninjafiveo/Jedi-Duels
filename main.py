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
        print(f"Hello I'm {self.name} nice to meet you im a jedi and i am a {self.rank}.")
       

    def lightsaber_attack(self, sith):
        damage=random.randint(10,30)
        sith.health-=damage
        print(f"{self.name} attacks {sith.name} with {self.lightsaber_color} dealing {damage } damage") 
        if sith.health<=0:
            print(f"{sith.name} has been defeated")
        else:
            print(f"{sith.name} has {sith.health} left...")

    def use_force(self,):
        print(f"{self.name} uses force attack to gain advantage")
class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"Hello I'm {self.name} nice to meet you im a sith and i am {self.rank}.")
       
    def lightsaber_attack(self, jedi):
        damage=random.randint(10,30)
        jedi.health-=damage
        print(f"{self.name} attacks {jedi.name} with {self.lightsaber_color} dealing {damage } damage")
        if jedi.health<=0:
            print(f"{jedi.name} has been defeated")
        else:
            print(f"{jedi.name}has {jedi.health} left...")

    def use_force(self,):
        print(f"{self.name} uses force attack to gain advantage")

# Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
       encounters = [
            "You found a Jedi!",
            "You ecountered a Sith!",
            " You found a holocron"
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
                sith.introduce()

        elif action == "duel":
            print("A duel has started!")
            print("Prepare for a lightsaber duel!")
            start_duel(jedi, sith)
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")
   
def start_duel(jedi,sith):
    jedi.lightsaber_attack(sith)
    sith.lightsaber_attack(jedi)
    print(f"Jedi {jedi.name} health : {jedi.health}")
    print(f"Jedi {sith.name} health : {sith.health}")
start_adventure()
