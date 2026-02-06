# Example 1
for x in ["a", "b", "c"]:
    if x == "b":
        break
    print(x)

# Example 2
for i in range(10):
    if i == 4:
        break
    print(i)

# Example 3
nums = [1, 3, 5, 7]
for n in nums:
    if n == 5:
        break
    print(n)

# Example 4
for i in range(1, 20):
    if i % 7 == 0:
        print(i)
        break

# Example 5
for i in range(5):
    if i == 3:
        break
else:
    print("No break")
