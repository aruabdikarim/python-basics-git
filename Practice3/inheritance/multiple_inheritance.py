# First parent class
class Father:
    def skill(self):
        print("Driving")

# Second parent class
class Mother:
    def talent(self):
        print("Cooking")

# Child inheriting from two parents
class Child(Father, Mother):
    pass

child = Child()
child.skill()
child.talent()