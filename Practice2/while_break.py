# Example 1
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# Example 2
x = 1
while True:
    if x % 5 == 0:
        print(x)
        break
    x += 1

# Example 3
nums = [1, 4, 6, 8]
for n in nums:
    if n == 6:
        break
    print(n)

# Example 4
attempts = 0
while attempts < 5:
    attempts += 1
    if attempts == 2:
        break
    print(attempts)

# Example 5
total = 0
i = 1
while i < 10:
    total += i
    if total > 15:
        break
    i += 1
print(total)
