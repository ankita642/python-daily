class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        print("adding new student in Database..")


s1 = Student("ankita", 97)
print(s1.name, s1.marks)

s2 = Student("ashwini", 88)
print(s2.name, s2.marks)