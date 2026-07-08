'''Define a Employee class with attributes role,department
& salary. This class also showDetails() method.
create an Engineer class that inherits properties from
Employee & has additional attribute: name & age. '''



class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("depertment=",self.department)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")       
        


e1 = Engineer("Ankita","20")
e1.showDetails()


