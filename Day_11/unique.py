#Write a functions which checks if all items are unique in the list.

def unique(fruits):
  len_list = len(fruits)
  set_fruits = set(fruits)
  len_set = len(set_fruits)

  if len_list == len_set:
    print("There are no duplicates!")
  else:
    print("There are duplicates!")

fruits = ["apple","banana", "kiwi"]
unique(fruits)