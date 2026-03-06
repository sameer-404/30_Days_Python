#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
"""
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""

num_one = int(input("Enter number one: "))
num_two = int(input("Enter number two: "))

if num_one > num_two:
  print(f"{num_one} is greater than {num_two}")
elif num_one < num_two:
  print(f"{num_two} is greater than {num_one}")
else:
  print(f"{num_one} and {num_two} are the same")
