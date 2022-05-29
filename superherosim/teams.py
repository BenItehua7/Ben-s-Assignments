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
    