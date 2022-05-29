from random import random

import random

class armor_class:
    def __init__(self, name, armor_strength):
        self.name = name
        self.armor_strength = armor_strength
    
    def __repr__(self): 
       return f'Armors({self.name}, {self.armor_strength})'

    def defend(self):
        block = random.randrange(0, self.armor_strength)

        return block
Armor1 = armor_class("strong defence", 100)
print(Armor1.defend())