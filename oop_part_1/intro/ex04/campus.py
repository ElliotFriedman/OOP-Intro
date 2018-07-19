from building import Building

class Campus ():
    def __init__ (self):
        self.buildings = 0
        self.capacity = 0

    def add_building(self, obj):
        self.buildings += 1
        self.capacity += obj.bcpcty

    def get_info(self):
        print("There are", self.buildings, "buildings with a total capacity of", self.capacity)
