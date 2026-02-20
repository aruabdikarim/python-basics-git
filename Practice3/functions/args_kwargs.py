# Function using *args to accept unlimited positional arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))

# Function using **kwargs to accept unlimited keyword arguments
def show_info(**info):
    for key, value in info.items():
        print(key, ":", value)

show_info(name="Asyl", age=20)

# Function combining *args and **kwargs
def order(item, *extras, **details):
    print("Item:", item)
    print("Extras:", extras)
    print("Details:", details)

order("Pizza", "Cheese", size="Large")

# Function looping through *args
def greet_many(*names):
    for name in names:
        print("Hello", name)

greet_many("Ali", "Dana", "Asyl")