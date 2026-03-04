#Chapter 6 - Tuples:
#A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, ().
#Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods.

#Methods related to tuples:

#1. tuple(): to create an empty tuple
#2. count(): to count the number of a specified item in a tuple
#3. index(): to find the index of a specified item in a tuple
#4. + operator: to join two or more tuples and to create a new tuple


#Creating a Tuple:

#Empty Tuple:
"""empty_tuple = ()
#or using empty_tuple = tuple()
print(len(empty_tuple))

#Tuple with initial value:
tpl = ("banana", "carrots", "ginger", "garlic")
print(len(tpl))"""

#Accessing Tuple items:
#Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items.
"""fruits = ("Banana", "lemon", "lime", "watermelon", "mango")
first_item = fruits[0]
second_item = fruits[1]
print(first_item)
print(second_item)
"""

#Negative indexing:
"""fruits = ("Banana", "lemon", "lime", "watermelon", "mango")
last_item = fruits[-1]
second_last = fruits[-2]
print(last_item)
print(second_last)"""

#Slicing Tuples:
#We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

"""fruits = ("banana", "mango", "kiwi", "lemon", "lime", "orange", "pineapple", "apple")
sliced_fruits = fruits[2:4]
print(sliced_fruits) #Same as lists but the output is tuple, thats all the difference there is

"""

#Changing tuples to a list:
#We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
"""fruits = ("banana", "mango", "kiwi", "lemon", "lime", "orange", "pineapple", "apple")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)
"""
#Basically whenever u want to change a value in tuple, change it back to list and change the value and change it back again to tuple


#Checking an item in a tuple:
#We can check if an item exists or not in a tuple using in, it returns a boolean.
"""
fruits = ("banana", "mango", "kiwi", "lemon", "lime", "orange", "pineapple", "apple")
result = "banana" in fruits
print(result)
fruits[0] = "horseraddish" #Throws error cause tuples doesnt support item assignment
print(fruits)
"""

#Joining Tuples:
#we can join two or more tuples using + operator:
"""fruits1 = ("apple", "banana", "orange")
fruits2 = ("lemon", "lime", "horseraddish")
fruits3 = ("pomelo", "carrots", "pineapple")

all_fruits = fruits1 + fruits2 + fruits3
print(all_fruits)"""


#Deleting Tuples:
#It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
"""tpl1 = ('item1', 'item2', 'item3')
del tpl1
print(tpl1) #Deleted so throws error"""

