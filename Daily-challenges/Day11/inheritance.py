# Base / Parent Class
class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_details(self):
        print(f"ID: {self.id_number}")
        print(f"Name: {self.name}")

# Derived / Child Class
class Developer(Employee):
    def __init__(self, name, id_number, language):
        # super() inherits and runs the parent class constructor
        super().__init__(name, id_number)
        self.language = language

    # Method Overriding: customizing parent behavior
    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.language}")

# Creating an instance of the child class
dev = Developer(name="Alice Smith", id_number="DEV104", language="Python")

# Executing the program
dev.display_details()
