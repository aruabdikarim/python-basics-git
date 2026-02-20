# Function returning one value
def square(number):
    return number ** 2

print(square(5))

# Function returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b

add, subtract, multiply = calculate(10, 4)
print(add)
print(subtract)
print(multiply)

# Function returning Boolean
def is_even(number):
    return number % 2 == 0

print(is_even(6))
print(is_even(7))

# Function returning a list
def get_squares(numbers):
    return [x ** 2 for x in numbers]

print(get_squares([1, 2, 3, 4]))