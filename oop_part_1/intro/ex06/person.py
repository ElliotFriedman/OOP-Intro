class Person():
    def __init__ (self):
        self.teacher = False
        self.student = False
    
    def is_student(self):
        return (self.student)
    
    def is_teacher(self):
        return (self.teacher)

class Student(Person):
    def __init__ (self):
        self.student = True
        self.teacher = False

class Teacher(Person):
    def __init__ (self):
        self.student = False
        self.teacher = True
