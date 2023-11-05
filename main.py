from rpg_classes.player import Player
from rpg_classes.archer import Archer
from game import *


def main():
    print("+------------- Welcome to Midare -------------+")
    print("|             Character Creation:             |")
    print("|                                             |")   
    print("|        1.  Create your character            |")
    print("|        2.  Exit the game                    |")
    print("+---------------------------------------------+")

    handle_input = int(input("What's your choice? "))
    match handle_input:
       case 1:
          print("\nCreating new character:")
          create_player()
          print("\nCharacter created!")
          start_game()
       case 2:
            print("Fodase")
       case _:
            print("Por favor, digite uma opção válida.")

main()
