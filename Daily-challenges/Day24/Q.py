'''Create a parent class called Employee with attributes name and
 base_salary. Add a method calculate_salary that simply returns
the base_salary.Create a child class called Manager that inherits
from Employee.The Manager should have an additional attribute
bonus.Use the super() function to initialize the parent 
attributes.Override calculate_salary so that it returns the
base_salary + bonus.'''

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

manager1 = Manager("ankita", "35k", "3k")
print(manager1.calculate_salary())

