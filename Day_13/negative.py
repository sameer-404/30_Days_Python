#Filter only negative and zero in the list using list comprehension

def filter(numbers):
  negative = [i for i in numbers if i < 1]
  return negative



numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = filter(numbers)
print(result)