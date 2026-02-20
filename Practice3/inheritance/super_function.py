# Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Child class using super()
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

emp = Employee("Asyl", 5000)
print(emp.name)
print(emp.salary)