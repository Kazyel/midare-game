from gameplay.game import create_hero, lobby
import time

def main():
        
    print("\n\n+--------------- Welcome to Midare ---------------+")
    print("|                                                 |")
    print("|            1.  Create your hero                 |")
    print("|            2.  About the game                   |")
    print("|            3.  Exit the game                    |")
    print("|                                                 |") 
    print("+-------------------------------------------------+")

    handle_input = int(input("What's your choice? > "))
    match handle_input:
        case 1:
            create_hero()
            lobby()
        case 2:
            pass
        case 3:
            print("Finishing the game process...")
            time.sleep(2)
        case _:
            print("Por favor, digite uma opção válida.")


main()
