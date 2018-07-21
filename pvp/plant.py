from organism import Organism
from card import Card

class Plant(Organism):
    cost = 35

    def __init__(self):
        super().__init__()
        self.powerup = 0

    def attack(self, nonplant):
        nonplant.hp -= self.dmg + self.powerup

    def apply_powerup(self, card):
        self.powerup += card.power

    def weaken_powerup(self):
        self.powerup /= 2



