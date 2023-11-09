class Weapon:
    def __init__(self, name, damage):
        self.damage = damage
        self.name = name

class Staff(Weapon): 
    def __init__(self, name="Wood Staff", damage=2):
        super().__init__(name, damage)

class Sword(Weapon):       
    def __init__(self, name="Wood Sword", damage=1):
        super().__init__(name, damage)
        
class Bow(Weapon):
    def __init__(self, name="Wood Bow", damage=2):
        super().__init__(name, damage)