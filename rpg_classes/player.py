class Player:
   def __init__(self, name, race, class_type):
      self.name = name
      self.__class_chosen = class_type
      self.race = race
   
   def update_name(self, new_name):
      self.name = new_name
   
   def get_class(self):
      return self.__class_chosen
   