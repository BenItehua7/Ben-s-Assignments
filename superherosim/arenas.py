class Arena:
    def __init__(self):
        team1_alive = 0
        team2_alive = 0
    def create_ability(self):
        name = input ("What is the ability name?")
        max_damage = input ("What is the max damage of the ability?")
        return ability(name,max_damage) 

    def create_weapon(self):
        weapon = input("What weapon would you like to make?")
        max_damage = input ("How much damage would you like to set for this weapon?")

        return (name,max_damage)

        pass

    def create_armor(self):
        armor = input ("What kind of armor would you like to give your hero?")
        armor_strength = input ("How much strength would you like to set this armor to")

        return (armor,armor_strength)

        pass

    def create_hero(self): 
        hero_name = input ("Hero's name: ")
        hero = hero (hero_name)
        add_item = None
        while add_item != "4"
            add_item = input ("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\Your choice:")
            if add_item == "1":

            elif add_item == "2":

            elif add_item == "3":
                

