#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
#We will be doing this:
"""
# Step 1 - map: square every number
# Step 2 - filter: keep only even ones
# Step 3 - reduce: add them all together
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def square(number):
    return number ** 2

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def add(x, y):
    return x + y

squared_numbers = list(map(square, numbers))
even_numbers = list(filter(is_even, squared_numbers))
total = reduce(add, even_numbers)

print(total)  # 560