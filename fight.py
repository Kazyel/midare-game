from rpg.enemy import Enemy
from rpg.classes import *
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
random_index = random.randint(0, len(dark_elf_names) - 1)
dark_elf = Enemy(dark_elf_names[random_index], "Dark Elf", Archer())
demon = Enemy(demon_names[random_index], "Demon", Warrior())
demi_god = Enemy(demi_gods_names[random_index], "Demi God", Mage())


def attack_elfs(class_choice):
    from game import lobby

    # Character Initialization
    player = class_choice
    # Characters
    enemy_char = dark_elf.class_type
    player_char = player.class_type
    # Damages
    player_damage = player_char.damage
    monster_damage = enemy_char.damage

    # Attack Menu
    print(f"\n   {dark_elf.race} {dark_elf.name}    ")
    print("                               ")
    print("     1. Attack                ")
    print("     2. Special Attack        ")
    print("     3. Run                   ")

    move = int(input("\nWhat you gonna do? "))

    match move:
        case 1:
            print("\nYou choose to use a normal attack:")
            print("--------------------------------------")
            print(
                f"> Enemy takes {enemy_char.take_damage(player_damage)} points of damage."
            )
            print(f"> You take {player_char.take_damage(monster_damage)} of damage.")
            print(f"\n| Monster HP: {enemy_char.check_death()}")
            print(f"| Your HP: {player_char.check_death()}")
            
            if enemy_char.health <= 0:
                gold_dropped = dark_elf.drop_gold()
                xp_dropped = dark_elf.drop_xp(1, 4)
                enemy_char.reset_hp(10)

                print("\n+---------------------------------------------+")
                print("|   You won the battle! Here's your reward:   |")
                print(
                f"|   You got: {player.gain_gold(gold_dropped)} gold and {player_char.gain_xp(xp_dropped)} experience          |"
                )
                print("+---------------------------------------------+")

                print("\nGoing back to the lobby...")
            
                player_char.check_level_up()
                lobby()

            else:
                attack_elfs(player)
        case 2:
            pass
        case 3:
            enemy_char.reset_hp(10)
            lobby()


def fight(class_choice):
    print("\n+--------------------------------+")
    print("|      Choose your opponent:     |")
    print("|                                |")
    print("|       1. Dark Elfs             |")
    print("|       2. Demons                |")
    print("|       3. Demi Gods             |")
    print("|       4. Final Boss            |")
    print("|                                |")
    print("+--------------------------------+")

    fight = int(input("Who is your opponent? "))
    match fight:
        case 1:
            attack_elfs(class_choice)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
