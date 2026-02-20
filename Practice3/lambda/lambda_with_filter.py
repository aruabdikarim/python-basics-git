numbers = [1, 2, 3, 4, 5, 6]

# Filtering even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Filtering numbers greater than 3
greater = list(filter(lambda x: x > 3, numbers))
print(greater)

# Filtering positive values
values = [-3, 4, -1, 6]
positive = list(filter(lambda x: x > 0, values))
print(positive)

# Filtering long names
names = ["Ali", "Alexander", "Dana"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(long_names)