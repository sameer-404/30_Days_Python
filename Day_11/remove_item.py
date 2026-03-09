#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(my_list, item):
  my_list.remove(item)
  return my_list

final_list = ["apple", "banana", "kiwi", "pomegranate"]
last_list = remove_item(final_list, "apple")
print(last_list)