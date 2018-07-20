from singly_list import SinglyList
from queue import queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card
import random

class Game():
    def __init__(self, file):
        with open(file, "r") as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(" ")]
            self.waves = Singly_List()
            self.waves_num = 0
            for line in iter(f.readline, ""):
                self.waves.add(Wave(*[int(x) for x in line.split(" ")]))
                self.waves_num += 1
        self.game_over = False
        self.turn_number = 0
        self.non_plants = 0

        self.deck = Stack()

        for i in range(100):
            self.deck.push(random.randint(1, 5))
        self.board = Queue()
        self.board.item = []
        for i in range(self.height):
            self.board.item.append([])
            for z in range(self.width):
                self.board.item[i].append(Queue())
                self.board.item[i][z].enqueue(".")

    def draw(self):
        print("Cash: $", self.cash, "\nWaves: ", self.waves_num, sep = "")
        s = " ".join([str(i) for i in range(self.width - 1)])
        print(" ", s)
        for row in range(self.height):
            s = []
            for col in range(self.width):
                if self.is_plant(row, col):
                    char = "P"
                elif self.is_nonplant(row, col):
                    size = self.board[row][col].size()
                    char = str(size) if size < 10 else "#"
                else:
                    char = "."
                s.append(char)
            print(row, " ", " ".join(s), "\n", sep="")
        print()

    def is_nonplant(self, row, col):

        if type(self.board.item[row][col]) == Non_Plant:
            return True
        else:
             False

    def is_plant(self, row, col):
        if type(self.board.item[row][col]) == Plant:
            return True
        else:
            False

    def remove(self, row, col):
        if is_nonplant(row, col):
            self.cash += self.board.item[row][col].front()
            self.non_plants -= 1
        self.board.item[row][col].dequeue()

    def place_nonplant(self, row):
        nplant = Non_Plant()
        self.board.item[row][self.width - 1].enqueue(nplant)
        self.non_plants += 1


