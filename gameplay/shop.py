from items.armor import *
from items.weapons import *


def shop(hero):
    from gameplay.game import city
    gold = hero.gold

    print("\n+------------- WELCOME TO THE SHOP --------------+")
    print("|                                                |")
    print("|      Hey, wanderer! Wanna buy an upgrade?      |")
    print("|                                                |")
    print("|             1. Swords                          |")
    print("|             2. Staffs                          |")
    print("|             3. Bows                            |")
    print("|             4. Armors                          |")
    print("|                                                |")
    print("|             5. Back to outside                 |")
    print("|                                                |")
    print("+------------------------------------------------+")

    while True:
        try:
            opt = int(input("What do you wanna buy? > "))
            match opt:
                case 1:
                    if hero.class_type.class_name == "Mage":
                        print(
                            "\nHow you gonna throw fireballs with a sword? Perhaps, I can sell you a sword?\n"
                        )
                    elif hero.class_type.class_name == "Archer":
                        print(
                            "\nIt's impossible (yet) to throw arrows with a sword. Maybe you wanna look a sword?\n"
                        )
                    else:
                        print("\n+------------------- TRADING --------------------+")
                        print("                                                ")
                        print("     Oh, there we go! Any sword that interests   ")
                        print("     this brave Warrior?                         ")
                        print("                                                ")
                        print("            1. Iron Sword [15 Gold]              ")
                        print("            2. Steel Sword [65 Gold]             ")
                        print("            3. Blessed Sword [96 Gold]           ")
                        print("            4. Ultimate Sword [145 Gold]         ")
                        print("                                                ")
                        print(f"            You have {gold} gold.                    ")
                        print("                                               ")
                        print("            5. Back to the shop menu            ")
                        print("                                                ")
                        print("+------------------------------------------------+")

                        while True:
                            try:
                                sword = int(
                                    input("So, do you wanna buy any of these? > ")
                                )
                                match sword:
                                    case 1:
                                        if (
                                            hero.gold >= 0
                                            and not hero.class_type.weapon_name
                                            == "Iron Sword"
                                        ):
                                            hero.class_type.set_weapon(
                                                Sword("Iron Sword", 3)
                                            )
                                            print(
                                                "\nYou bought a Iron Sword! Your base damage increased to 3.\n"
                                            )
                                        elif (
                                            hero.class_type.weapon_name == "Iron Sword"
                                        ):
                                            print("\nYou already bought this one!\n")
                                        else:
                                            print(
                                                "\nSorry, you don't have enough money to buy this one, go and work more!\n"
                                            )

                                    case 2:
                                        if (
                                            hero.gold >= 40
                                            and not hero.class_type.weapon_name
                                            == "Steel Sword"
                                        ):
                                            hero.class_type.set_weapon(
                                                Sword("Steel Sword", 6)
                                            )
                                            print(
                                                "\nYou bought a Steel Sword! Your base damage increased to 6.\n"
                                            )
                                        elif (
                                            hero.class_type.weapon_name == "Steel Sword"
                                        ):
                                            print("\nYou already bought this one!\n")
                                        else:
                                            print(
                                                "\nSorry, you don't have enough money to buy this one, go and work more!\n"
                                            )
                                    case 3:
                                        if (
                                            hero.gold >= 40
                                            and not hero.class_type.weapon_name
                                            == "Blessed Sword"
                                        ):
                                            hero.class_type.set_weapon(
                                                Sword("Blessed Sword", 12)
                                            )
                                            print(
                                                "\nYou bought a Blessed Sword! Your base damage increased to 12.\n"
                                            )
                                        elif (
                                            hero.class_type.weapon_name == "Blessed Sword"
                                        ):
                                            print("\nYou already bought this one!\n")
                                        else:
                                            print(
                                                "\nSorry, you don't have enough money to buy this one, go and work more!\n"
                                            )
                                    case 4:
                                        if (
                                            hero.gold >= 150
                                            and not hero.class_type.weapon_name
                                            == "Ultimate Sword"
                                        ):
                                            hero.class_type.set_weapon(
                                                Sword("Ultimate Sword", 500)
                                            )
                                            print(
                                                "\nYou bought the Ultimate Sword! Your base damage increased to 500.\n"
                                            )
                                        elif (
                                            hero.class_type.weapon_name == "Steel Sword"
                                        ):
                                            print("\nYou already bought this one!\n")
                                        else:
                                            print(
                                                "\nSorry, you don't have enough money to buy this one, go and work more!\n"
                                            )
                                    case 5:
                                        print(
                                            "\nThat's fine, feel free to look everything!"
                                        )
                                        shop(hero)
                                    case _:
                                        print("\nPlease, enter a valid option!\n")
                            except ValueError:
                                print(
                                    "\nWe only accept numbers, please enter a integer!\n"
                                )
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print("\nGoing back to the city...")
                    city()
                case _:
                    print("\nPlease, enter a valid option!\n")
        except ValueError:
            print("\nWe only accept numbers, please enter a integer!\n")
