from rpg.classes import Archer, Warrior, Mage
from rpg.player import Player
from fight import *

class_choice = None


def create_player():
    print("\n Creating a new character:")
    print("+-------------------------+")
    name = input("  Enter your name: ")
    race = input("  Enter you race: ")

    print("+-------------------------+")
    print("|    Choose your class:   |")
    print("|    1. Warrior           |")
    print("|    2. Archer            |")
    print("|    3. Mage              |")
    print("+-------------------------+")

    choice = int(input("> "))

    global class_choice
    match choice:
        case 1:
            class_choice = Player(name, race, Warrior())
            return class_choice
        case 2:
            class_choice = Player(name, race, Archer())
            return class_choice
        case 3:
            class_choice = Player(name, race, Mage())
            return class_choice
        case _:
            choice = int(input("Please, enter a valid input: "))

    print("\nCharacter created!")
    print("------------------")
    print(f"Name: {class_choice.name}")
    print(f"Race: {class_choice.race}")
    print(f"Class: {class_choice.get_class().class_name}")


def check_stats():
    player = class_choice.class_type

    print("\n+=-=-=-= Your Stats =-=-=-=+")
    print(f"   {class_choice.name}, The {player.class_name}")
    print(f"   Level: {player.level}")
    print(f"   XP: {player.xp}")
    print(f"   Health: {player.health}")
    print(f"   Damage: {player.damage}")
    print(f"   Armor: {player.armor}")
    print(f"   Gold: {class_choice.get_gold()}")
    print(f"   XP needed for next level: {((player.level * 4) + player.level / 2)}")


def lobby():
    print("\n+-------------- Midare Setsugekka ---------------+")
    print("|           1.  Fight                            |")
    print("|           2.  Shop                             |")
    print("|           3.  Check your stats                 |")
    print("|           4.  Exit the game                    |")
    print("+------------------------------------------------+")
    handle_input = int(input("What you want to do? "))

    match handle_input:
        case 1:
            fight(class_choice)
        case 2:
            pass
        case 3:
            check_stats()
            lobby()
        case 4:
            exit()
        case _:
            handle_input = int(input("Please, enter a valid input:"))
