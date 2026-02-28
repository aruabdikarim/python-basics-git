import math
import random

nums = [4, 7, -3, 9, 2]

# --- BUILT-IN ---
print(min(nums))   # smallest
print(max(nums))   # largest
print(abs(-10))    # absolute value
print(round(3.6))  # round
print(pow(2, 3))   # 2^3

# --- MATH MODULE ---
print(math.sqrt(16))        # square root
print(math.ceil(3.2))       # up
print(math.floor(3.8))      # down
print(math.sin(math.pi/2))  # 1
print(math.cos(0))          # 1
print(math.pi)
print(math.e)

# --- RANDOM ---
print(random.random())        # 0..1 float
print(random.randint(1, 10))  # int
print(random.choice(nums))    # random element

random.shuffle(nums)          # shuffle list
print(nums)