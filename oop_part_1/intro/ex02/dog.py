from animal import Animal

class Dog(Animal):
    def __init__ (self):
        print("Creating a dog")
    
    def speak (self):
        print("Rooooof Rooof!")

    def sleep (self):
        print("Zzzzzzz")
