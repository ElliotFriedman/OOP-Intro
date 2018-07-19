from person import Person
from person import Student
from person import Teacher
from classroom import ClassRoom

room = ClassRoom(10)


stu = Student()
t = Teacher()

room.p_mod(stu)
room.p_mod(t)

room.print_class()
