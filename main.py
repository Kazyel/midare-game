from rpg_classes.player import Player 
from rpg_classes.archer import Archer 

def main():
   print("+------------- Welcome to Midare -------------+")
   print("|        1.  Create your character            |")
   print("|        2.  Choose the difficulty            |")
   print("|        3.  Exit the game                    |")
   print("+---------------------------------------------+")

   new_player = Player("Isa", "Humana", Archer())
   print("\n" + new_player.name)
   print(new_player.race)
   print(f"A sua classe é: {new_player.get_class().class_type}\nSeu HP é: {new_player.get_class().health}\nE seu nível é {new_player.get_class().level} ")


main()