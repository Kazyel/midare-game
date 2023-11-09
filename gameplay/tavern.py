from gameplay.game import city


def tavern(hero):
    player = hero.class_type
    gold = hero.gold
    gold_tax = int((hero.class_type.level * 3) // 1.5)

    print("\n+------------ WELCOME TO THE TAVERN -------------+")
    print("|                                                |")
    print("|             1. Sleep (Recover HP)              |")                                                 
    print("|             2. Back to outside                 |")
    print("|                                                |")
    print("+------------------------------------------------+")

    while True:
        try:
            opt = int(input("What will you do? > "))
            match opt:
                
                case 1:
                    print("\n+-------------- TAVERN KEEPER --------------+")
                    print("|                                           |")
                    print("|      Hello, wanderer! Do you want to      |")
                    print("|      stay for the night? I can do a       |")
                    print(f"|      generous price for you!              |")
                    print("|                                           |")
                    print(f"|            It will be {gold_tax} gold.             |")
                    print(f"|             You have {gold} gold.              |")
                    print("|                                           |")
                    print("+-------------------------------------------+")

                    while True:
                        choice = str(input("Pay for the night (Y/N)? > ")).lower()
                        
                        try:
                            match choice:
                                case "y":
                                    if (
                                        player.health < player.max_health
                                        and gold > gold_tax
                                    ):
                                        hero.lose_gold(gold_tax)
                                        player.set_full_health()
                                        print(
                                            f"\nYou paid {gold_tax} gold for the night and were healed to full life.\n"
                                        )
                                        tavern(hero)
                                    elif gold <= gold_tax:
                                        print(
                                            "\nYou don't have enough money for the night.\n"
                                        )
                                    elif player.health == player.max_health:
                                        print("\nYou are already at full life.\n")
                                        tavern(hero)
                                case "n":
                                    print(
                                        f"\n{hero.name}: No, thanks, I will pass the offer...\n"
                                    )
                                    tavern(hero)
                                case _:
                                    print("\nPlease, enter a valid option!\n")
                        except ValueError:
                            print("\nPlease, only enter with characters!\n")

                case 2:
                    print("\nGoing back to the city...")
                    city()
                case _:
                    print("\nPlease, enter a valid option!\n")

        except ValueError:
            print("\nWe only accept numbers, please enter a integer!\n")
