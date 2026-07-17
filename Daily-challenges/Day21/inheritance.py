class Car:
    color = "black"
    @staticmethod
    def start():
        print("car is started...")

    @staticmethod
    def stop():
        print("car is stopped")

class ToyotaCar(Car):
    def __init__(self,name):
      self.name = name
    
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.color)
    
        
    