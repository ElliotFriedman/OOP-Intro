from organism import Organism

class Non_Plant(Organism):
    worth = 20
    
    def __init__(self):
        self.hp = 80
        self.dmg = 5

    def attack(self, plant):
        plant.hp -= self.dmg
