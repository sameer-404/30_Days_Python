#Define a call function before map, filter or reduce, see examples:

def square(num):
    return num ** 2

numbers = [1,2,3,4,5]
result = list(map(square,numbers))
print(result)


def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5]
result = list(filter(is_even, numbers))
print(result)

from functools import reduce

def add(x,y):
    return x + y

numbers = [1,2,3,4,5]
result = reduce(add, numbers)
print(result)