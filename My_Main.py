import random


class Adventure:
    def random_encounter(self):
        encounters = [
            "You Found A Jedi!",
            "You Encountered A Sith!",
            "You Found A Holocron!"
        ]
        return random.choice(encounters)
    def start_duel(jedi, sith):
        print("A duel has started!")
        jedi.lightsaber_attack(sith)
        sith.lightsaber_attack(jedi)
        print(f"Jedi {jedi.name} health: {jedi.health}")
        print(f"Sith {sith.name} health: {sith.health}")
def start_adventure():
    print("Welcome to the Star Wars Adventure!")
    player_name = input("Enter your name, traveler: ")
    adventure = Adventure(player_name)

    jedi = jedi("Luke Skywalker", "Green", "Master")
    sith = sith("Darth Vader", "Red", "Lord")

    while True:
        action = input("What would you like to do? (explore/duel/quit): ").lower()

        if action == "explore":
            encounter = adventure.random_encounter()
            print(encounter)
            if "Jedi" in encounter:
                jedi.introduce()
            elif "Sith" in encounter:
                sith.introduce()
        elif action == "duel":
            start_duel(jedi, sith) # type: ignore

        elif action == "quit":
            print("May the Force be with you. Goodbye!")
            break

        else:
            print("Invalid action, try again.")