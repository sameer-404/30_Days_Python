#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
"""
print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
"""

def evens_and_odds(num):
  num_even = 0
  num_odd = 0

  for i in range(num+1):
    if i % 2 == 1:
      num_odd += 1
    else:
      num_even += 1
  return num_even, num_odd
  
result_even, result_odd = evens_and_odds(100)
print(f"The num of evens: {result_even} and num of odds: {result_odd}")