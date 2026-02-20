# Class demonstrating different types of methods
class Car:

    # Class variable
    wheels = 4

    # Constructor
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # Instance method
    def drive(self):
        print(self.brand, "is driving at", self.speed, "km/h")

    # Class method
    @classmethod
    def vehicle_type(cls):
        print("All cars have", cls.wheels, "wheels")

    # Static method
    @staticmethod
    def general_info():
        print("Cars are used for transportation")

car1 = Car("Toyota", 120)

car1.drive()
Car.vehicle_type()
Car.general_info()