from rpg.enemy import Enemy
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
dark_elf = Enemy(dark_elf_names[random_name], "Dark Elf", Archer())
demon = Enemy(demon_names[random_name], "Demon", Warrior())
demi_god = Enemy(demi_gods_names[random_name], "Demi God", Mage())

round_count = 1

def monster_fight(hero, enemy_type):
    from gameplay.game import lobby
    global round_count 
    
    # Character Initialization
    player = hero
    enemy = enemy_type
    # Characters
    enemy_class = enemy.class_type
    player_class = player.class_type
    # Damages
    player_damage = player_class.damage
    monster_damage = enemy_class.damage

    # Attack Menu
    print(f"\n{enemy.race} {enemy.name} - Round: {round_count}    ")
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
                f"> Enemy takes {enemy_class.take_damage(player_damage)} points of damage."
            )
            print(f"> You take {player_class.take_damage(monster_damage)} of damage.")
            print(f"\n| Monster HP: {enemy_class.check_death()}")
            print(f"| Your HP: {player_class.check_death()}")
            time.sleep(2)
            
            if enemy_class.health <= 0:
                gold_dropped = gold_drop(enemy)
                xp_dropped = xp_drop(enemy)

                print("\n+---------------------------------------------+")
                print("|   You won the battle! Here's your reward:   |")
                print(
                f"|   You got: {player.gain_gold(gold_dropped)} gold and {player_class.gain_xp(xp_dropped)} experience          |"
                )
                print("+---------------------------------------------+")

                player_class.check_level_up()
                monster_hp_reset(enemy)
                round_count = 1
                
                print("\nGoing back to the lobby...")
                lobby()
                
            elif player_class.health <= 0:
                print("+----------------------+")
                print("|      You Died!       |")
                print("+----------------------+")
                exit()
            else: 
                round_count += 1
                monster_fight(player, enemy)
        case 2:
            pass
        case 3:
            monster_hp_reset(enemy)
            lobby()

def gold_drop(enemy_type):
    if enemy_type.race == "Dark Elf":
        return enemy_type.drop_gold(2, 6)
    elif enemy_type.race == "Demon":
        return enemy_type.drop_gold(12, 25)
    else:
        return enemy_type.drop_gold(30, 45)
    
def xp_drop(enemy_type):
    if enemy_type.race == "Dark Elf":
        return enemy_type.drop_xp(1, 4)
    elif enemy_type.race == "Demon":
        return enemy_type.drop_xp(8, 14)
    else:
        return enemy_type.drop_gold(15, 22)

def monster_hp_reset(enemy_type):
    if enemy_type.race == "Dark Elf":
        return enemy_type.class_type.reset_hp()
    elif enemy_type.race == "Demon":
        return enemy_type.class_type.reset_hp()
    else:
        return enemy_type.class_type.reset_hp()

def fight(hero):
    from gameplay.game import lobby
    
    print("\n+--------------------------------+")
    print("|      Choose your opponent:     |")
    print("|                                |")
    print("|       1. Dark Elfs             |")
    print("|       2. Demons                |")
    print("|       3. Demi Gods             |")
    print("|       4. Final Boss            |")
    print("|                                |")
    print("|       5. Back                  |")
    print("|                                |")
    print("+--------------------------------+")

    opt = int(input("Who is your opponent? "))
    match opt:
        case 1:
            monster_fight(hero, dark_elf)
        case 2:
            monster_fight(hero, demon)
        case 3:
            monster_fight(hero, demi_god)
        case 4:
            lobby()
