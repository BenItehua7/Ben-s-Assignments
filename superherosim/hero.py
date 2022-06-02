import random
from unicodedata import name
from ability import Ability 
from armor import armor_class
from weapon import weapon
from teams import teams 


class Hero:


  def __init__(self, name = "Hero", starting_health=100):
    '''Instance properties:
      name: Hero
      starting_health: integer
      current_health: integer
    '''

    self.name = name 
    
    self.starting_health = starting_health

    self.current_health = starting_health 

    self.armor =[]

    self.ability= []

  def __repr__(self):
    return f'hero?({self.name}, {self.starting_health}) '

  def add_ability(self,ability):
    self.ability.append(ability)
    return self.ability


  def attack(self):
    attack_value = 0
    for ability in self.ability:
      attack_value += ability.attack()
    print(f"{self.name} has {attack_value} attack")

    return attack_value


  def take_damage(self, incoming_damage):
    damage = incoming_damage - self.defend()
    if damage >= 0: 
      self.current_health -= damage

  def add_armor(self,armor):
    self.armor.append(armor)
    return self.armor 

  
    

  def defend(self):
    defend_value = 0
    for armor in self.armor:
      defend_value += armor.defend()
    print(f"{self.name} has {defend_value} defend")
    return defend_value



  


  def add_weapon(self,weapon):
    self.weapon.append(weapon)
    print(f"{self.name}") (f"{self.weapon}")
    return self.add_weapon
      

  def add_kill(self):
      self.add_kill += 1


  def add_death(self):
      self.add_death += 1



  def battle(self , opponent):
    ''' Current Hero will take turns battling the opponent hero passed in.
    '''
    if not self.ability and not opponent.ability:
      print("These heroes cannot fight, they have no abilities")

    fight = True
    while fight:

      print (f"{self.name}: {self.current_health}")
      print (f"{opponent.name}: {opponent.current_health}")

      self.take_damage(opponent.attack())
      opponent.take_damage(self.attack())



      if self.current_health <= 0:
       print (f"{opponent.name} Winner")
       fight = False

      elif opponent.current_health <= 0:
       print (f"{self.name} Winner")
       fight = False

    # TODO: battle each hero until a victor emerges.
    # Phases to implement:
    #1) randomly choose winner, print the name of the victor
    # Hint: Look into random library, more specifically the choice method

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("The Flash")
    hero2 = Hero("Reverse Flash")

    #hero1.battle(hero1) 
    ability1 = Ability("bark", 100)
    hero1.add_ability(ability1)
    hero2.add_ability(ability1)

    #print(hero1.attack())

    armor1 = armor_class("pants", 100)

    hero1.add_armor(armor1)
    hero2.add_armor(armor1)

    hero1.battle(hero2)