class Building ():
    def __init__ (self, name, capacity):
        self.bname = name
        self.bcpcty = capacity

    def get_info(self):
        print("Building \"",self.bname, "\" can hold", self.bcpcty, "people")

