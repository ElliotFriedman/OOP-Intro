from building import Building
from campus import Campus

obj = Campus()

mathb = Building("MATH BUILDING", 300)
mathb.get_info()



sci = Building("Science BUILDING", 700)
sci.get_info()

obj.add_building(mathb)
obj.get_info()

obj.add_building(sci)
obj.get_info()
