# Example 1: Menu
choice = 2
if choice == 1:
    print("Start")
elif choice == 2:
    print("Settings")
elif choice == 3:
    print("Exit")
else:
    print("Unknown")

# Example 2: Day number
day = 6
if day == 1:
    print("Monday")
elif day == 6:
    print("Saturday")
else:
    print("Other day")

# Example 3: Command dictionary
cmd = "run"
commands = {"run": "Running", "stop": "Stopping"}
print(commands.get(cmd, "Unknown command"))

# Example 4: Calculator
op = "+"
a = 3
b = 4
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)

# Example 5: Language choice
lang = "en"
if lang == "en":
    print("Hello")
elif lang == "ru":
    print("Привет")
else:
    print("Unknown language")
