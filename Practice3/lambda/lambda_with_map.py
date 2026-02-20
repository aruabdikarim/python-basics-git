numbers = [1, 2, 3, 4]

# Using map to square numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Using map to convert numbers to strings
strings = list(map(lambda x: str(x), numbers))
print(strings)

# Using map to increase prices
prices = [100, 200, 300]
updated = list(map(lambda x: x * 1.1, prices))
print(updated)

# Using map to capitalize names
names = ["ali", "dana"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(capitalized)