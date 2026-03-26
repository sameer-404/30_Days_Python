#Use reduce to sum all the numbers in the numbers list.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def add(x,y):
  return x + y

sum_numbers = reduce(add, numbers)
print(sum_numbers)