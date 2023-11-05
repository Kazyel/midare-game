class Player:
    def __init__(self, name, race, class_type):
        self.name = name
        self.class_type = class_type
        self.race = race
        self.__gold = 0

    def get_gold(self):
        return self.__gold

    def gain_gold(self, qnt):
        self.__gold += qnt
        return qnt

    def lose_gold(self, qnt):
        self.gold -= qnt
