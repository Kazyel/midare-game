from rpg.classes import *
from gameplay.fight import *
from rpg.player import Player
import time

# Global Hero Instance
hero = None


def create_hero():
    # Character Created Display Message
    def character_created(hero):
        print("\nCharacter created!")
        print("------------------")
        print(f"Name: {hero.name}")
        print(f"Race: {hero.race}")
        print(f"Class: {hero.class_type.class_name}")
        print("\nStarting game...")

    print("\n\n        CREATING A NEW HERO")
    print("   +---------------------------+")
    name = input("       Enter your name: ")
    race = input("       Enter your race: ")

    print("\n+------- CHOOSE YOUR CLASS -------+")
    print("|                                 |")
    print("|          1. Warrior             |")
    print("|          2. Archer              |")
    print("|          3. Mage                |")
    print("|                                 |")
    print("+---------------------------------+")
    while True:
        try:
            opt = int(input("> "))
            global hero
            match opt:
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
                    input("\nPlease, enter a valid input!\n")
        except ValueError:
            print("\nWe only accept numbers, please enter a integer!\n")


def check_stats():
    hero_class = hero.class_type

    print("\n+=-=-=-=+=-=-=+ YOUR STATS +=-=-=+=-=-=-=+")
    print("                                        |")
    print(f"   Level: {hero_class.level}                             ")
    print(
        f"|   EXP ({((hero_class.level * 4) + hero_class.level // 2) - hero_class.xp} more to level up): {hero_class.xp}          |"
    )
    print(f"   Health: {hero_class.health}                            ")
    print(f"   Damage: {hero_class.damage}                            ")
    print(f"   Armor: {hero_class.armor}                             ")
    print(f"   Total Gold: {hero.gold}                        ")
    print("                                        ")
    print("+=-=-=-=+=-=-=-=+=-=-=-=+=-=-=-=+=-=-=-=-+")


def city():
    from gameplay.tavern import tavern

    # time.sleep(3)
    print("\n+-------------- CITY OF SETSUGEKKA --------------+")
    print("|                                                |")
    print("|           1.  Fight                            |")
    print("|           2.  Shop                             |")
    print("|           3.  Tavern                           |")
    print("|           4.  Check your stats                 |")
    print("|                                                |")
    print("|           5.  Exit the game                    |")
    print("|                                                |")
    print("+------------------------------------------------+")
    while True:
        try:
            opt = int(input("What you want to do? > "))
            match opt:
                case 1:
                    fight(hero)
                case 2:
                    pass
                case 3:
                    tavern(hero)
                case 4:
                    check_stats()
                    city()
                case 5:
                    print("\nFinishing the game process...")
                    time.sleep(2)
                    exit()
                case _:
                    print("\nPlease, enter a valid option!\n")
        except ValueError:
            print("\nWe only accept numbers, please enter a integer!\n")
