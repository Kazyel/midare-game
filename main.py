from gameplay.game import create_hero, city
from rpg.classes import *
import time
from items.armor import * 

def main():

    print("\n\n+--------------- WELCOME TO MIDARE ---------------+")
    print("|                                                 |")
    print("|             1.  Create your hero                |")
    print("|             2.  About the game                  |")
    print("|             3.  Exit the game                   |")
    print("|                                                 |")
    print("+-------------------------------------------------+")
    while True:
        try:
            handle_input = int(input("What's your choice? > "))
            match handle_input:
                case 1:
                    create_hero()
                    city()
                case 2:
                    pass
                case 3:
                    print("Finishing the game process...")
                    time.sleep(2)
                case _:
                    print("\nPlease, enter a valid option!\n")
        except ValueError:
            print("\nWe only accept numbers, please enter a integer!\n")


main()
