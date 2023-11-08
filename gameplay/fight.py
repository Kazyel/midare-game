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
dark_elf = Enemy(dark_elf_names[random_name], "Dark Elf", Archer(10, 1, 1))
demon = Enemy(demon_names[random_name], "Demon", Warrior(25, 6, 4))
demi_god = Enemy(demi_gods_names[random_name], "Demi God", Mage(50, 12, 7))

round_count = 1


def monster_fight(hero, enemy_type):
    from gameplay.game import city
    player = hero
    enemy = enemy_type

    monster_class = enemy.class_type
    player_class = player.class_type

    player_damage = player_class.damage
    monster_damage = monster_class.damage

    print("\n+--------- FIGHT STARTED ---------+")
    print(f"\n| {enemy.race} {enemy.name}")
    print(f"| HP: {monster_class.health} \n| DMG: {monster_class.damage} \n| ARMOR: {monster_class.armor}")    
    
    # Attack Menu
    def fight_moves():
        global round_count
        
        print(f"\n+---------- YOUR STATS -----------+")
        print(f"|     HP: {player_class.health} | DMG: {player_damage} | ARMOR: {player_class.armor}  |")
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
                        print("You use a normal attack:")
                        if(monster_class.take_damage(player_damage) == 1):
                            print(f"-> {enemy.name} takes {monster_class.take_damage(player_damage)} point of damage.")
                        else:
                            print(f"-> {enemy.name} takes {monster_class.take_damage(player_damage)} points of damage.")
            
                        print(f"\n{enemy.name} attacks you:")
                        if monster_class.health > 0:
                            if(player_class.take_damage(monster_damage) == 1):
                                print(f"-> You take {player_class.take_damage(monster_damage)} point of damage.")
                            else:
                                print(f"-> You take {player_class.take_damage(monster_damage)} points of damage.")
                        
                        print(f"\n| {enemy.name} HP: {monster_class.death_check()}")
                        print(f"| Your HP: {player_class.death_check()}")
                        print("+--------------------------------------+\n")
                        # time.sleep(2)

                        if monster_class.health <= 0 and not player_class.health <= 0:
                            gold_dropped = gold_drop(enemy)
                            xp_dropped = xp_drop(enemy)

                            print("\n+------------------------------------------------+")
                            print("|   You won the battle! Here's your reward:      |")
                            print(
                                f"|   You got: {player.gain_gold(gold_dropped)} gold and {player_class.gain_xp(xp_dropped)} points of experience   |"
                            )
                            print("+------------------------------------------------+")

                            player_class.check_level_up()
                            monster_class.reset_hp()
                            round_count = 1

                            print("\nGoing back to the city...")
                            city()

                        elif player_class.health <= 0:
                            print("\n+----------------------+")
                            print("|      YOU DIED!       |")
                            print("+----------------------+")
                            exit()
                        else:
                            round_count += 1
                            fight_moves()
                    case 2:
                        pass
                    case 3:
                        monster_class.reset_hp()
                        print(f"\nYou cowardly run away from {enemy.name},")
                        print("And returns back to the city...")
                        city()
                    case _:
                        print("\nPlease, enter a valid movement!\n")
            except ValueError:
                print("\nWe only accept numbers, please enter a valid integer!\n")
    fight_moves()


def gold_drop(enemy_type):
    if enemy_type.race == "Dark Elf":
        return enemy_type.drop_gold(2, 6)
    elif enemy_type.race == "Demon":
        return enemy_type.drop_gold(12, 25)
    else:
        return enemy_type.drop_gold(30, 45)


def xp_drop(enemy_type):
    if enemy_type.race == "Dark Elf":
        return enemy_type.drop_xp(2, 4)
    elif enemy_type.race == "Demon":
        return enemy_type.drop_xp(8, 14)
    else:
        return enemy_type.drop_gold(15, 22)


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
