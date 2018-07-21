import pdb
from singly_list import SinglyList
from queue import Queue
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
            self.waves = SinglyList()
            self.waves_num = 0
            for line in iter(f.readline, ""):
                self.waves.add_head(Wave(*[int(x) for x in line.split(" ")]))
                self.waves_num += 1
        self.game_over = False
        self.turn_number = 0
        self.non_plants = 0

        self.deck = Stack()

        for i in range(100):
            self.deck.push(random.randint(1, 5))

        self.board = [] #SinglyList Next points to the next array.
                        #Data points to the list that stores the queues

        for i in range(self.height):
            self.board.append([]) #;
            for z in range(self.width):
                self.board[i].append(Queue())
                print(self.board[i][z])

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
        print(self.board[row][col].isEmpty())
        if type(self.board[row][col].front()) == Non_Plant:
            return True
        else:
            False

    def is_plant(self, row, col):
        if type(self.board[row][col]) == Plant:
            return True
        else:
            False

    def remove(self, row, col):
        print("Total amount of non_plants", self.non_plants)
        print("cash before removal", self.cash)
        if self.is_nonplant(row, col) == True:
            self.non_plants -= 1
        self.cash += self.board[row][col].front().worth

        #else:
        #    self.cash += 35
        print("cash after removal", self.cash)
        self.board[row][col].dequeue()
        print("Total amount of non_plants", self.non_plants)


    def place_nonplant(self, row):
        nplant = Non_Plant()
        self.board[row][self.width - 1].enqueue(nplant)
        self.non_plants += 1

    def place_plant(self, row, col):
        if col != self.width - 1 and self.is_nonplant(row, col) == False and self.is_plant(row, col) == False:
            plant = Plant()
            self.board.item[row][col].enqueue(plant)
            self.cash -= Plant.cost



