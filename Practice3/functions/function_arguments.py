# Function with positional arguments
def multiply(a, b):
    return a * b

print(multiply(3, 4))

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

# Function using keyword arguments
def describe(name, age):
    print(name, "is", age, "years old")

describe(age=20, name="Asyl")

# Function accepting list as argument
def sum_numbers(numbers):
    return sum(numbers)

print(sum_numbers([1, 2, 3, 4]))