'''Create a parent class Vehicle with attributes brand and
 max_speed, and a method display_info(). Create a child class
 Bus that inherits from Vehicle but adds a seating_capacity 
attribute. Override display_info() to include this new capacity.'''

class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def display_info(self):
        return f"Brand: {self.brand}, Max Speed: {self.max_speed} km/h"

class Bus(Vehicle):
    def __init__(self, brand, max_speed, seating_capacity):
        # Initialize parent attributes
        super().__init__(brand, max_speed)
        self.seating_capacity = seating_capacity

    def display_info(self):
        # Leverage parent string and add custom details
        parent_info = super().display_info()
        return f"{parent_info}, Capacity: {self.seating_capacity} seats"

# Testing
school_bus = Bus("Volvo", 100, 50)
print(school_bus.display_info())
# Output: Brand: Volvo, Max Speed: 100 km/h, Capacity: 50 seats
    