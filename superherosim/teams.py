import random
from unicodedata import name
from hero import Hero

class team:
    def __init__(self,name):
        self.name = name
        self.heroes = []
        self.deaths = 0
        self.kills = 0

    def add_hero(self,hero):
        self.heroes.append(hero)
        return self.heroes

    def remove_hero(self,hero):
        self.heroes.remove(hero)
        return self.heroes

    def view_all_heroes(self):
        for item in self.heroes:
            print(item) 
    
    def add_kill(self):
        self.add_kill += 1

    def add_death(self):
        self.add_death += 1
    
    def team_attack(self,another_team):
        another_team = random.choice (another_team.heroes)
        print(f"{another_team}")
        self = random.choice(self.heroes)
        print (f"{self}")

        if self.deaths >= 0:
          print (f"{self} is ready to fight!")
        elif self.deaths <= 1:
           print(f"{self} can no longer compete")

    def revive (self):
        self.current_health = 100
        self.death = 0