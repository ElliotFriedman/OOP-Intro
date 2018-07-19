from person import Person

class ClassRoom():
    def __init__ (self, capacity):
        self.teacher = 0
        self.student = 0
        self.capacity = capacity

    def p_mod(self, p):
        if p.is_student():
            print(p.is_student())
            self.student += 1
        elif p.is_teacher():
            self.teacher += 1

    def print_class(self):
        print("The classroom has a capacity of", self.capacity)
        print("There are", self.teacher, "teachers and" , self.student, "students")
