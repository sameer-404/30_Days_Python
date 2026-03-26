#Use for to print each number in the numbers list.

numbers = [4, 8, 15, 16, 23, 42, 7, 3, 19, 55,
           31, 66, 72, 9, 28, 47, 83, 11, 37, 64]


"""for number in numbers:
  print(number)
"""

#Use map to create a new list by changing each number to its square in the numbers list

def square(number):
  return number ** 2

result = list(map(square, numbers))
print(result)