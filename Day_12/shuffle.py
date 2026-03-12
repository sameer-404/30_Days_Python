#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(my_list):
  shuffled = sorted(my_list, key=lambda x: random.random())
  return shuffled

original = [1,2,3,4,5,6]
print(original)
result = shuffle_list(original)
print(result)

