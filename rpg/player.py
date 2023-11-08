class Player:
    def __init__(self, name, race, class_type):
        self.name = name
        self.class_type = class_type
        self.race = race
        self.gold = 0

    def gain_gold(self, qnt):
        self.gold += qnt
        return qnt

    def lose_gold(self, qnt):
        self.gold -= qnt
