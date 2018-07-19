from player import Player

class Striker(Player):
    def run_play(self, index):
        if index < 3:
            print(self.playbook[index])
        else:
            print(index, "Is not a valid play for a striker")

class Defender(Player):
    def run_play(self, index):
        if index > 2 and index < 5:
            print(self.playbook[index])
        else:
            print(index, "Is not a valid play for a defender")
