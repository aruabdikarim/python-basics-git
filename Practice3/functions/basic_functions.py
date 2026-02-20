# Function without parameters
def greet():
    print("Welcome to Python")

greet()

# Function with one parameter
def greet_user(name):
    print("Hello", name)

greet_user("Asyl")

# Function returning a value
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))

# Function with multiple return values
def calculate(a, b):
    return a + b, a - b

result_add, result_sub = calculate(10, 4)
print(result_add)
print(result_sub)