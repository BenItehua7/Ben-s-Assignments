import random

class Ability:

    def __init__(self,name,max_damage=100):
        self.name = name
        self.max_damage = max_damage

    def attack (self):
        attack_value =random.randrange(0,self.max_damage)
        print(attack_value)

        return attack_value

ability = Ability("Super Speed", 100)
ability.attack 