from rpg_classes.classes import Archer, Warrior, Mage
from rpg_classes.player import Player

class_choice = None

def create_player():
   print("\nCreating new character:")
   name = input("Enter your name: ")
   race = input("Enter you race: ")
   
   print("+-------------------------+")
   print("|    Choose your class:   |")
   print("|    1. Warrior           |")
   print("|    2. Archer            |")
   print("|    3. Mage              |")
   print("+-------------------------+")
   
   choice = int(input("What's your choice? "))   
   
   global class_choice
   match choice:
      case 1:
         class_choice = Player(name, race, Warrior())
         return class_choice
      case 2:
         class_choice = Player(name, race, Archer())
         return class_choice
      case 3: 
         class_choice = Player(name, race, Mage())
         return class_choice
      case _:
         choice = int(input("Please, enter a valid input: "))

   print("\nCharacter created!")
   print("------------------")
   print(f"Name: {class_choice.name}")
   print(f"Race: {class_choice.race}")
   print(f"Class: {class_choice.get_class().class_name}")
   
def check_stats():
    print("\n+=-=-=-= Your Stats =-=-=-=+") 
    print(f"   {class_choice.name}, The {class_choice.get_class().class_name}")
    print(f"   Level: {class_choice.get_class().level}")
    print(f"   Health: {class_choice.get_class().health}")
    print(f"   Damage: {class_choice.get_class().get_damage()}")
    print(f"   Armor: {class_choice.get_class().get_defense()}")
    print(f"   XP needed for next level: {class_choice.get_class().level * 4}")

def start_game():
    print("\n+-------------- Midare Setsugekka ---------------+")
    print("|           1.  Fight                            |")
    print("|           2.  Check your stats                 |")
    print("|           3.  Exit the game                    |")
    print("+------------------------------------------------+")
    handle_input = int(input("What's your choice? "))
    
    match handle_input:
       case 1:
          pass
       case 2:
          check_stats()
       case 3:
          exit()
       case _:
          handle_input = int(input("Please, enter a valid input:"))
    
