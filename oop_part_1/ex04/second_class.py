from first_class import FirstClass
import random

class SecondClass(FirstClass):
    def __init__ (self, name):
        print("Hello", name)

    def roll_dice(self, name):
        print("Method roll_dice in SecondClass called")
        self.say_hello(name, random.randint(1, 6))
