class ClassType:
    def __init__(self, health, base_damage, base_armor):
        self.level = 1
        self.xp = 1
        self.health = health
        self.__base_damage = base_damage
        self.__base_armor = base_armor
    
    def set_xp(self, xp_gain):
        self.xp += xp_gain

    def level_up(self):
        self.level += 1
        
    def check_level_up(self):
        actual_xp = self.xp

        if actual_xp > self.level * 4:
            self.level_up()
            return f"You leveled up! Now, your level is {self.level}."
        else:
            return f"You can't level up yet! You need more {self.level * 4} experience."
    
    def get_defense(self):
        return self.__base_armor
    
    def get_damage(self):
        return self.__base_damage


class Archer(ClassType):
    def __init__(self):
        super().__init__(10, 2, 1)
        self.class_name = "Archer"
 
class Warrior(ClassType):
    def __init__(self):
        super().__init__(15, 1, 2)
        self.class_name = "Warrior"
        
class Mage(ClassType):
    def __init__(self):
        super().__init__(7, 3, 1)
        self.class_name = "Warrior"
    

