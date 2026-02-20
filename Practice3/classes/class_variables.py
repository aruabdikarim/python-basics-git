# Class demonstrating class vs instance variables
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)
print(dog2.species)

dog1.species = "Modified"

print(dog1.species)
print(dog2.species)