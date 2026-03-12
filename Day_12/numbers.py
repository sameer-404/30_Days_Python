#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def seven():
  my_set = set()
  

  while len(my_set) < 7:
    my_set.add(random.randint(0,9))
  return list(my_set)

print(seven())



