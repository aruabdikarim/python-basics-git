# Parent class
class Animal:
    def speak(self):
        print("Animal sound")

# Child class overriding method
class Dog(Animal):
    def speak(self):
        print("Dog says Woof")

dog = Dog()
dog.speak()