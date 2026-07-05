
class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def drive(self):
        return f"The {self.brand} {self.model} is driving!"


car1 = Car("Tata", "Nexon")
car2 = Car("Mahindra", "Thar")

print(car1.drive())  
print(car2.drive())  