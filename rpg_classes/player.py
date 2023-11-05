class Player:
   def __init__(self, name, class_chosen, race):
      self.__name = name
      self.__class_chosen = class_chosen
      self.__race = race
      
   def get_name(self):
      return self.__name
   
   def set_name(self, name):
      self.__name = name
      
   