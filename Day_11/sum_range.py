#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num):
  total = 0
  for i in range(num+1):
    total += i
  return total

print(sum_of_numbers(100))