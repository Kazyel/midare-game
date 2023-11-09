class Armor:
    def __init__(self, name, defense):
        self.defense = defense
        self.name = name
        
class Cloth(Armor):
    def __init__(self, name="Cloth Armor", defense=0):
        super().__init__(name, defense)

class Chainmail(Armor):
    def __init__(self, name="Chainmail Armor", defense=3):
        super().__init__(name, defense)

class Leather(Armor):
    def __init__(self, name="Leather Armor", defense=1):
        super().__init__(name, defense)