#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "orange", "mango")
vegatables = ("cucumber", "carrot", "cabbage", "potatoes")
animal_products = ("meat", "fish", "eggs", )
groceries_tp = fruits + vegatables + animal_products
print(groceries_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
groceries_ls = list(groceries_tp)
print(groceries_ls)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
length = len(groceries_ls)
print(length)

if length % 2 == 1:
  print("The groceries is odd!")
  middle_index = length // 2
  print(f"The middle item is {groceries_ls[middle_index]}")
else:
  print("The groceries is even!")
  middle_index1 = length // 2
  middle_index2 = (length//2) -1
  print(f"The middle items are {groceries_ls[middle_index1]} and {groceries_ls[middle_index2]}")


