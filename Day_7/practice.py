#Day 7 - Sets

#Creating Sets:
#Creating empty set:
st = set()

#Creating sets with initial value:
fruits = {"banana", "orange", "mango", "apple"}

"""#getting sets length:
length = len(fruits)
print(f"The length of set fruits is: {length}")


#Accessing items in a set:
#we will use loops to access items, will see this in loop section

#Checking an item:
#same as lists and tuple
result = "banana" in fruits
print(result)"""

#Adding item to a set:
#Once a set is created we cannot change any item, we can only add additional items

"""fruits.add("lime")
print(fruits)

#To add multiple items we use update() method,
#update() method takes list as arguments
fruits.update(["cucumber", "pomegranate", "dragonfruit"])
print(fruits)
"""
#Alternate method we can create a list or tuple and update that into a set
#for example:
"""
vegetables = ("tomato", "potato", "cabbage")
fruits.update(vegetables)
print(fruits)"""

#Removing items from a set:

#we can remove an item from a set using remove() method.
#If the item is not found remove() will throw errors so its good to check if the item exists or not:

"""result = "banana" in fruits
print(result)
#checked now ready to remove
fruits.remove("banana")
print(fruits)"""

#we can also use pop() method to remove items :
"""fruits.pop()
print(fruits)
#but since pop() method takes no arguments, we cant remove the specific element in a set, it just randomly picks for us

#Also if we are interested in the removed item, we can assign it to the method and it will display the popped item
popped_item = fruits.pop()
print(popped_item)
print(fruits)"""


#Randomly pops cause there is no index in sets !!! - VVV important

#Clearing items in a set:
#If you want to cleare or empty the set we can use clear method!
"""fruits.clear()
print(fruits)
#Output set() --- empty set"""


#Deleting a set:
#just use del set_name to delete the set
"""del fruits
#print(fruits).  #Will throw an error!"""


#Converting List to a set:
#we can convert a list into a set and vice versa just add list() and set to convert them
#Important:
#Converting list to set removed duplicates and only unique items will be reversed, so its important to remember
#for example:
"""vegetables = ['tomato', 'potato', 'cabbage','onion', 'carrot','carrot','cabbage','carrot']
print(vegetables)
vegetables = set(vegetables)
print(vegetables)
#removed all the duplicates, and now we can assign it back to list , if we want
vegetables = list(vegetables)
print(vegetables)"""


#Joining sets:
#We can join two sets using union(). or update()
#vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
"""groceries = fruits.union(vegetables)
print(groceries)"""

#update() inserts a set into a given set:
"""fruits.update(vegetables)
print(fruits)
"""



#Set Operations:
#Finding Intersection items:
#Intersection returns a set of items which are in both the sets
#intersection() or & operator:
"""whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection_of_both = whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(intersection_of_both)"""

"""python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
inter= python&dragon
print(inter)"""