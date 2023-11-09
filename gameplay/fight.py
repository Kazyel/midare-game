from rpg.enemy import *
from rpg.classes import *
import time
import random

# Enemy Names
dark_elf_names = ["Sakryn Shrundri", "Zathe Novne", "Ghyta Arva", "Rhadok Yazaer"]
demon_names = ["Kogmas", "Ar'gaxium", "Azgodoth", "Malmanog"]
demi_gods_names = [
    "Vumis, Daughter of Passion",
    "Vylren, Son of Hatred",
    "Phozon, Born of the Flame",
    "Athos, Guardian of Vyx",
]

# Enemy Characters
random_name = random.randint(0, len(dark_elf_names) - 1)
dark_elf = DarkElf(dark_elf_names[random_name])
demon = Demon(demon_names[random_name])
demi_god = DemiGod(demi_gods_names[random_name])

round_count = 1


def monster_fight(hero, enemy_type):
    from gameplay.game import city

    hero_class = hero.class_type
    hero_damage = hero_class.get_damage()
    enemy = enemy_type
    enemy_damage = enemy.damage

    print("\n+--------- FIGHT STARTED ---------+")
    print(f"\n| {enemy.race} {enemy.name}")
    print(f"| HP: {enemy.health} \n| DMG: {enemy.damage} \n| ARMOR: {enemy.armor}")

    # Attack Menu
    def fight_moves():
        global round_count

        print(f"\n+---------- YOUR STATS -----------+")
        print(
            f"|     HP: {hero_class.health} | DMG: {hero_damage} | ARMOR: {hero_class.armor}   |"
        )
        print("+------------- MOVES -------------+")
        print("|                                 |")
        print("|        1. Attack                |")
        print("|        2. Special Attack        |")
        print("|        3. Run                   |")
        print("|                                 |")
        print("+---------------------------------+")

        while True:
            try:
                move = int(input("What you gonna do? "))
                match move:
                    case 1:
                        print("\n\n+------------- BATTLE LOG -------------+")
                        print("| You use a normal attack:")
                        if hero_class.deal_damage(enemy) == 1:
                            print(
                                f"| -> {enemy.name} takes {hero_class.deal_damage(enemy)} point of damage."
                            )
                        else:
                            print(
                                f"| -> {enemy.name} takes {hero_class.deal_damage(enemy)} points of damage."
                            )
                        print("| ")
                        print(f"| {enemy.name} attacks you:")
                        if enemy.health > 0:
                            if hero_class.take_damage(enemy_damage) == 1:
                                print(
                                    f"| -> You take {hero_class.take_damage(enemy_damage)} point of damage."
                                )
                            else:
                                print(
                                    f"| -> You take {hero_class.take_damage(enemy_damage)} points of damage."
                                )
                        print("| ")
                        print(f"| {enemy.name} HP: {enemy.death_check()}")
                        print(f"| Your HP: {hero_class.death_check()}")
                        print("+--------------------------------------+\n")
                        # time.sleep(2)

                        if enemy.health <= 0 and not hero_class.health <= 0:
                            gold_dropped = enemy.drop_gold()
                            xp_dropped = enemy.drop_xp()

                            print(
                                "\n+------------------------------------------------+"
                            )
                            print("    You won the battle! Here's your reward:      ")
                            print(
                                f"    You got: {hero.gain_gold(gold_dropped)} gold and {hero_class.gain_xp(xp_dropped)} points of experience   "
                            )
                            print(
                                "+------------------------------------------------+\n"
                            )

                            hero_class.check_level_up()
                            enemy.set_full_health()
                            round_count = 1

                            print("\nGoing back to the city...")
                            city()

                        elif hero_class.health <= 0:
                            print("\n+----------------------+")
                            print("|      YOU DIED!       |")
                            print("+----------------------+\n")
                            enemy.set_full_health()
                            city()
                        else:
                            round_count += 1
                            fight_moves()
                    case 2:
                        pass
                    case 3:
                        enemy.set_full_health()
                        print(f"\nYou cowardly run away from {enemy.name},")
                        print("And returns back to the city...")
                        city()
                    case _:
                        print("\nPlease, enter a valid movement!\n")
            except ValueError:
                print("\nWe only accept numbers, please enter a valid integer!\n")

    fight_moves()


def fight(hero):
    from gameplay.game import city

    print("\n+------------ FIGHTS ------------+")
    print("|                                |")
    print("|       1. Dark Elfs             |")
    print("|       2. Demons                |")
    print("|       3. Demi Gods             |")
    print("|       4. Final Boss            |")
    print("|                                |")
    print("|       5. Back                  |")
    print("|                                |")
    print("+--------------------------------+")

    while True:
        try:
            opt = int(input("Who do you wanna fight? > "))
            match opt:
                case 1:
                    monster_fight(hero, dark_elf)
                case 2:
                    monster_fight(hero, demon)
                case 3:
                    monster_fight(hero, demi_god)
                case 4:
                    pass
                case 5:
                    print("\nGoing back to the city...")
                    city()
                case _:
                    print("\nPlease, enter a valid option!\n")
        except ValueError:
            print("\nWe only accept numbers, please enter a integer!\n")
