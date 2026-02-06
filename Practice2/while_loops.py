# Example 1
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Countdown
n = 3
while n > 0:
    print(n)
    n -= 1

# Example 3: Sum
total = 0
x = 1
while x <= 5:
    total += x
    x += 1
print(total)

# Example 4: Boolean condition
run = True
count = 0
while run:
    print(count)
    count += 1
    if count == 3:
        run = False

# Example 5: Length check
words = ["", "hi", "hello"]
i = 0
while i < len(words) and len(words[i]) < 2:
    i += 1
print(words[i])
