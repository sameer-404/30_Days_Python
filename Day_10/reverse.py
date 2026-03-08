#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ["banana", "orange", "mango", "lemon"]

reversed_fruits = []

for i in range(len(fruits)-1, -1, -1):
  reversed_fruits.append(fruits[i])

print(reversed_fruits)