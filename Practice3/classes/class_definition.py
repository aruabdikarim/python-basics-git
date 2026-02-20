# Basic class definition
class Person:
    def say_hello(self):
        print("Hello")

person = Person()
person.say_hello()

# Class with attributes
class Car:
    brand = "Toyota"

car = Car()
print(car.brand)

# Modifying object property
car.brand = "BMW"
print(car.brand)

# Deleting property
del car.brand