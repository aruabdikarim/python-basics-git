# Example 1: Basic boolean values
# True and False are boolean values in Python
print(True)
print(False)

# Example 2: bool() from numbers
# Non-zero numbers are True, zero is False
print(bool(1))   # True
print(bool(0))   # False

# Example 3: bool() from strings
# Non-empty strings are True, empty string is False
print(bool("Hello"))  # True
print(bool(""))       # False

# Example 4: bool() from collections
# Non-empty collections are True, empty collections are False
print(bool([1, 2, 3]))  # True
print(bool([]))         # False

# Example 5: Custom object truthiness
# The object is True if it contains items
class Box:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return self.items > 0

print(bool(Box(3)))  # True
print(bool(Box(0)))  # False
