import random

class Enemy:
    def __init__(self, name, race, class_type):
        self.name = name
        self.race = race
        self.class_type = class_type

    def drop_gold(self, x, y):
        return random.randint(x, y)

    def drop_xp(self, x, y):
        return random.randint(x, y)
