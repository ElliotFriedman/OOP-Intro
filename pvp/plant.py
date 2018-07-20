from organism import Organism

class Plant(Organism):
    cost = 35

    def __init__(self):
        super().__init__()
        self.powerup = 0

    def attack(self, nonplant):
        nonplant.hp -= self.dmg + self.powerup

    def apply_powerup(self, card):
        self.powerup += card

    def weaken_powerup(self, card):
        self.powerup /= 2



