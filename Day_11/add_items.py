#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(my_list, item):
  my_list.append(item)
  return my_list

final_list = ["Potato", "Pumpkin", "Apple"]
result = add_item(final_list,"Chicken")
print(result)