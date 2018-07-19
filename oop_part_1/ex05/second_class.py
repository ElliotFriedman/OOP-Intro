from first_class import FirstClass
import random

class SecondClass(FirstClass):
    hobby = "Null"
    def __init__ (self, name, hobb):
        print("Hello", name)
        self.hobby = hobb

    def roll_dice(self, name):
        print("Method roll_dice in SecondClass called")
        self.say_hello(name, random.randint(1, 6))

    def get_hobby(self):
        return (self.hobby)
