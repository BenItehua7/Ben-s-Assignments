import random

class Ability:

    def __init__(self,name,max_damage):
        self.name = name
        self.max_damage = max_damage

    def __repr__(self):
        return f'Ability({self.name}, {self.max_damage})'

    def attack (self):
        attack_value = random.randrange(0,self.max_damage)

        return attack_value

ability1 = Ability("Super Speed",100)
print (ability1.attack()) 