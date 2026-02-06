# Example 1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Example 2
n = 0
while n < 10:
    n += 1
    if n % 2 != 0:
        continue
    print(n)

# Example 3
words = ["", "ok", "", "yes"]
i = 0
while i < len(words):
    if words[i] == "":
        i += 1
        continue
    print(words[i])
    i += 1

# Example 4
nums = [1, -2, 3]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# Example 5
i = 0
while i < 5:
    i += 1
    if i == 1:
        continue
    print(i)
