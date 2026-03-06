#The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
your_fruit = input("Enter your fruit: ")

if your_fruit in fruits:
  print("That fruit already exist in the list")
else:
  print("Your fruit doesn't exist, here's the revised list!")
  fruits.append(your_fruit)
  print(fruits)