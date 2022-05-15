
import random

class Hero:


  def __init__(self, name ="Hero", starting_health=1000):
    '''Instance properties:
      name: Hero
      starting_health: integer
      current_health: integer
    '''

    self.name = name 
    
    self.starting_health = starting_health

    self.current_health = starting_health 

  def battle(self, opponent):
    ''' Current Hero will take turns battling the opponent hero passed in.
    '''
    heroes_names = []
    heroes_names.append(self.name)
    heroes_names.append(opponent.name)

    winner = random.choice (heroes_names)
    print(winner)
    # TODO: battle each hero until a victor emerges.
    # Phases to implement:
    #1) randomly choose winner, print the name of the victor
    # Hint: Look into random library, more specifically the choice method

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("The Flash")
    hero2 = Hero("Reverse Flash")

    hero1.battle(hero2)