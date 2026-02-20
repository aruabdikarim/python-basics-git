# Parent class
class Animal:
    def speak(self):
        print("Animal sound")

# Child class inheriting from Animal
class Dog(Animal):
    pass

dog = Dog()
dog.speak()