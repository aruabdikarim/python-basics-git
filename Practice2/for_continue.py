# Example 1
for x in ["a", "b", "c"]:
    if x == "b":
        continue
    print(x)

# Example 2
for i in range(10):
    if i % 2 == 1:
        continue
    print(i)

# Example 3
words = ["a", "hi", "hello"]
for w in words:
    if len(w) < 2:
        continue
    print(w)

# Example 4
nums = [1, -1, 2]
for n in nums:
    if n < 0:
        continue
    print(n)

# Example 5
for i in range(1, 16):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
