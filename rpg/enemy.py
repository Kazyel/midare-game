import random


class Enemy:
    def __init__(self, name):
        self.name = name

    def drop_gold(self, x, y):
        return random.randint(x, y)

    def drop_xp(self, x, y):
        return random.randint(x, y)

    def set_full_health(self):
        self.health = self.full_health

    def death_check(self):
        if self.health <= 0:
            return "Dead"
        return self.health


class DarkElf(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 10
        self.full_health = 10
        self.damage = 2
        self.armor = 1
        self.race = "Dark Elf"

    def drop_gold(self):
        return super().drop_gold(2, 6)

    def drop_xp(self):
        return super().drop_xp(1, 4)


class Demon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 25
        self.full_health = 25
        self.damage = 6
        self.armor = 5
        self.race = "Demon"

    def drop_gold(self):
        return super().drop_gold(12, 25)

    def drop_xp(self):
        return super().drop_xp(9, 14)


class DemiGod(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 45
        self.full_health = 45
        self.damage = 12
        self.armor = 8
        self.race = "Demi God"

    def drop_gold(self):
        return super().drop_gold(30, 45)

    def drop_xp(self):
        return super().drop_xp(14, 23)
