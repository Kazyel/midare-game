class Archer():
   def __init__(self):
      self.class_type = "Archer"
      self.level = 1
      self.__xp = 0
      self.__base_damage = 2
      self.__base_armor = 1
      self.health = 10
  
   def set_xp(self, xp_gain):
      self.__xp += xp_gain
  
   def level_up(self):
      self.level += 1
   
   def check_level_up(self):
      actual_xp = self.__xp
      
      if(actual_xp > self.level * 4):
         self.level_up()
         return f"You leveled up! Now, your level is {self.level}."
      else:
         return f"You can't level up yet! You need more {self.level * 4} experience."