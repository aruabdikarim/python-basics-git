# Simple lambda function
square = lambda x: x ** 2
print(square(4))

# Lambda with two parameters
add = lambda a, b: a + b
print(add(3, 5))

# Lambda used inside another function
def apply_operation(x, func):
    return func(x)

print(apply_operation(10, lambda x: x * 3))

# Lambda replacing simple function
double = lambda x: x * 2
print(double(7))