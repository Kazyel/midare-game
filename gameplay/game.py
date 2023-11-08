from rpg.classes import *
from gameplay.fight import *
from rpg.player import Player
import time

# Global Hero Instance
hero = None


def create_hero():
    print("\n\n    Creating a new hero:")
    print("+--------------------------+")
    name = input("\n Enter your name: ")
    race = input(" Enter your race: ")

    print("\n+--------------------------+")
    print("|    Choose your class:    |")
    print("|                          |")
    print("|      1. Warrior          |")
    print("|      2. Archer           |")
    print("|      3. Mage             |")
    print("|                          |")
    print("+--------------------------+")

    choice = int(input("> "))
    global hero
    match choice:
        case 1:
            hero = Player(name, race, Warrior())
            character_created(hero)
            return hero
        case 2:
            hero = Player(name, race, Archer())
            character_created(hero)

            return hero
        case 3:
            hero = Player(name, race, Mage())
            character_created(hero)
            return hero
        case _:
            choice = int(input("Please, enter a valid input: "))

    # Character Created Display Message
    def character_created(hero):
        print("\nCharacter created!")
        print("------------------")
        print(f"Name: {hero.name}")
        print(f"Race: {hero.race}")
        print(f"Class: {hero.class_type.class_name}")
        print("\nStarting game...")


def check_stats():
    player_class = hero.class_type

    print("\n+=-=-=-= Your Stats =-=-=-=+")
    print(f"   {hero.name}, The {player_class.class_name}")
    print(f"   Level: {player_class.level}")
    print(f"   EXP: {player_class.xp}")
    print(f"   Health: {player_class.health}")
    print(f"   Damage: {player_class.damage}")
    print(f"   Armor: {player_class.armor}")
    print(f"   Gold: {hero.gold}")


def lobby():
    time.sleep(3)
    print("\n+-------------- Midare Setsugekka ---------------+")
    print("|           1.  Fight                            |")
    print("|           2.  Shop                             |")
    print("|           3.  Check your stats                 |")
    print("|           4.  Exit the game                    |")
    print("+------------------------------------------------+")
    handle_input = int(input("What you want to do? > "))

    match handle_input:
        case 1:
            fight(hero)
        case 2:
            pass
        case 3:
            check_stats()
            lobby()
        case 4:
            print("Finishing the game process...")
            time.sleep(2)
            exit()
        case _:
            handle_input = int(input("Please, enter a valid input:"))
