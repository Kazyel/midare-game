class ClassType:
    def __init__(self, health, base_damage, base_armor):
        self.level = 1
        self.xp = 0
        self.health = health
        self.damage = base_damage
        self.armor = base_armor
    
    def __level_up(self):
        self.level += 1
    
    def __reset_xp(self):
        self.xp = 0

    def take_damage(self, damage):
        self.health -= damage - (self.armor / 2)
        return damage - (self.armor / 2)

    def gain_xp(self, xp_gain):
        self.xp += xp_gain
        return xp_gain

    def check_level_up(self):
        actual_xp = self.xp
        if actual_xp >= ((self.level * 4) + self.level / 2):
            self.__level_up()
            self.__reset_xp
        else: 
            return False

    def check_death(self):
        if self.health <= 0:
            return "Dead"
        return self.health

    def reset_hp(self, health):
        self.health = health


class Archer(ClassType):
    def __init__(self):
        super().__init__(10, 2, 1)
        self.class_name = "Archer"
        self.energy = 3

    def rain_of_arrows(self):
        self.energy -= 2
        return 4

    def upgrade_energy(self):
        self.energy += 2


class Warrior(ClassType):
    def __init__(self):
        super().__init__(15, 5, 2)
        self.class_name = "Warrior"
        self.stamina = 4

    def cyclone(self):
        self.stamina = 4

    def upgrade_stamina(self):
        self.stamina += 4


class Mage(ClassType):
    def __init__(self):
        super().__init__(7, 2, 1)
        self.class_name = "Warrior"
        self.mana = 2

    def fireball(self):
        self.mana -= 2
        return 6

    def upgrade_mana(self):
        self.mana += 4
