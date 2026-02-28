# --- ITERATOR with iter() and next() ---
numbers = [1, 2, 3, 4, 5]

it = iter(numbers)   # convert list → iterator
print(next(it))      # get next element (1)
print(next(it))      # (2)
print(next(it))      # (3)


# --- LOOP THROUGH ITERABLE ---
for num in numbers:  # for uses iterator internally
    print(num)


# --- CUSTOM ITERATOR ---
class CountUp:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self      # iterator object

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration  # end of iteration


for x in CountUp(5):
    print(x)  # 1..5


# --- GENERATOR FUNCTION ---
def square_generator(n):
    for i in range(n):
        yield i * i   # return values one by one


for val in square_generator(5):
    print(val)


# --- GENERATOR EXPRESSION ---
gen_exp = (x * 2 for x in range(5))  # lazy generator

for val in gen_exp:
    print(val)