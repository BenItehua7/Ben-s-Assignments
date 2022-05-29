import random

from ability import Ability

class weapon(Ability):
     def attack(self):
        attack_value = random.randrange(int (self.max_damage / 2),self.max_damage)
        return attack_value

weapon1 = weapon('Lighting sword',100)
print (weapon1.attack())