import math


class ClassType:
    def __init__(self, health, damage, armor):
        self.level = 1
        self.xp = 0
        self.health = health
        self.max_health = health
        self.damage = damage
        self.armor = armor

    def __level_up(self):
        self.level += 1
        self.armor += 1
        self.damage += 1
        self.health += 2
        self.max_health += 2

    def take_damage(self, dmg):
        damage_taken = math.ceil(dmg - (self.armor / 2))
        if damage_taken >= 0:
            self.health -= damage_taken
            return damage_taken
        return 0

    def death_check(self):
        if self.health <= 0:
            return "Dead"
        return self.health

    def gain_xp(self, xp_gain):
        self.xp += xp_gain
        return xp_gain

    def check_level_up(self):
        actual_xp = self.xp
        if actual_xp >= ((self.level * 4) + self.level // 2):
            self.__level_up()
            self.xp = 0
        else:
            return False

    def set_full_health(self):
        self.health = self.max_health


class Archer(ClassType):
    def __init__(self, health=15, damage=3, armor=1):
        super().__init__(health, damage, armor)
        self.class_name = "Archer"
        self.energy = 4

    def rain_of_arrows(self):
        self.energy -= 2
        return self.damage * 2

    def upgrade_energy(self):
        self.energy += 2


class Warrior(ClassType):
    def __init__(self, health=20, damage=1, armor=3):
        super().__init__(health, damage, armor)
        self.class_name = "Warrior"
        self.stamina = 4

    def cyclone(self):
        self.stamina -= 2
        return self.damage * 3

    def upgrade_stamina(self):
        self.stamina += 4


class Mage(ClassType):
    def __init__(self, health=10, damage=2, armor=0):
        super().__init__(health, damage, armor)
        self.class_name = "Warrior"
        self.mana = 2

    def fireball(self):
        self.mana -= 2
        return self.damage * 4

    def upgrade_mana(self):
        self.mana += 4
