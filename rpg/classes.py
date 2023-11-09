import math
from items.weapons import *
from items.armor import *


class ClassType:
    def __init__(self, health, weapon, armor):
        self.level = 1
        self.xp = 0
        self.health = health
        self.max_health = health
        self.damage = weapon.damage
        self.armor = armor.defense
        self.weapon_name = weapon.name
        self.armor_name = armor.name

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

    def set_weapon(self, weapon):
        self.damage = weapon.damage
        self.weapon = weapon.name
    
    def set_armor(self, armor):
        self.damage = armor.defense
        self.weapon = armor.name


class Archer(ClassType):
    def __init__(self, health=15, weapon=Bow(), armor=Leather()):
        super().__init__(health, weapon, armor)
        self.class_name = "Archer"
        self.weapon_type = "Bow"
        self.armor_type = "Leather"
        self.energy = 4

    def skill(self):
        self.energy -= 2
        return ["Rain of Arrows", self.damage * 2]

    def upgrade_energy(self):
        self.energy += 2

class Warrior(ClassType):
    def __init__(self, health=20, weapon=Sword(), armor=Chainmail()):
        super().__init__(health, weapon, armor)
        self.class_name = "Warrior"
        self.weapon_type = "Sword"
        self.armor_type = "Chainmail"
        self.stamina = 4

    def skill(self):
        self.stamina -= 2
        return ["Cyclone", self.damage * 3]

    def upgrade_stamina(self):
        self.stamina += 4

class Mage(ClassType):
    def __init__(self, health=10, weapon=Staff(), armor=Cloth()):
        super().__init__(health, weapon, armor)
        self.class_name = "Mage"
        self.weapon_type = "Staff"
        self.armor_type = "Cloth"
        self.mana = 2

    def skill(self):
        self.mana -= 2
        return ["Fireball", self.damage * 4]

    def upgrade_mana(self):
        self.mana += 4