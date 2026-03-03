#Lists:

#In python we can create list in two ways:

#First:
#Using the built in function list()
"""lst = list()
print(len(lst))"""

#Second:
#Using square brackets:
"""lst = []
print(len(lst))"""

#We use len() to find the length of a list:
'''#for example:
fruits = ['banana', 'orange', 'mango', 'lemon']  #list of fruits

vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']   #list of vegetables

animal_products = ['milk', 'meat', 'butter', 'yoghurt']    

web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']

#Print the lists and its length:
print(f"Fruits: {len(fruits)}")
print(f"Vegetables: {len(vegetables)}")
print(f"Animal Products: {len(animal_products)}")
print(f"Web Technologies: {len(web_techs)}")'''

"""#Lists can have items of different data types:
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types"""

"""#Acessing list items using positive indexing:
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]"""

#unpacking list items:
"""fruits = ["banana", "orange", "mango", "lemon", "lime", "apple"]
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)"""

"""countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)"""


# Slicing Items from a list:
#Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
"""
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4] #it returns all the fruits
#this will also give the same result as one above
all_fruits = fruits[0:]   #if we dont set where to stop it takes all the rest
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[1::2]   #here we used a 3rd argument, step. It will take every 2nd item - ["banana", "mango"]
print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)"""

"""fruits = ["banana", "lemon", "mango", "orange", "lime", "watermelon", "pineapple", "kiwi", "pomegranate"]
selected = fruits[1::2]
print(selected)"""


#Modifying the list:
"""fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avacado"
print(fruits) 
#now changing the second item in list from orange to apple
fruits[1] = "apple"
print(fruits)

#now changing the last item of the list
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)"""

#Checking items in a list:
"""fruits = ["banana", "apple", "lemon", "lime"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "cucumber" in fruits
print(does_exist)
"""

#Adding items to a list:
"""fruits = ["banana", "lime", "mango"]
print(fruits)
print(f"Before adding length: {len(fruits)}")
fruits.append("orange")
print(fruits)
print(f"After adding orange list length: {len(fruits)}")"""


#Inserting items into a list:
"""fruits = ["banana", "orange", "mango"]
fruits.insert(1, "apple")
print(fruits)
print(len(fruits))"""

#Removing items from a list
#remove() method

"""fruits = ["banana", "Kiwi", "banana", "lemon", "mango"]
fruits.remove("banana")
print(fruits)"""
#remove method only removes the first occurance of the item in that list

#pop() method:
#the pop() method remove the specified index, if not specified , it removes the last item of that list
"""fruits = ["banana", "kiwi", "orange", "mango", "lemon"]
fruits.pop(2)
print(fruits)"""

#del() method
#the del keyword remove the specified index and it can also be used to delete items within index range.
#it can also delete the list completely
"""
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1:3]
#this delets the items between given indexes, so it doesnt delete the item with the index 3
print(fruits)"""

#Copying the list:
"""fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)"""

#Joining Lists:
#There are several ways to join, or concatenate, two or more lists:

#plus(+) operator:
"""positive_number = [1,2,3,4,5]
zero = [0]
negative_number = [-5,-4,-3,-2,-1]
integers = negative_number + zero + positive_number
print(integers)"""

#Joining using extend() method:
#The extend method allows us to append list in a list
"""num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print(f"Numbers: {num1}")"""

#Counting items in a list:
#The count() method returns the number of times an item appears in a list:
"""fruits = ["banana", "orange", "mango", "mango"]
print(fruits.count("banana"))  #1
print(fruits.count("mango"))   #2
"""



#finding index of an item:
"""fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))
print(fruits.index("lemon"))"""

#Reversing the list:
"""fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)"""


#Sorting list items:
#Using sort() method:
"""fruits = ["banana", "kiwi", "pomegranate", "lemon", "mango", "orange"]
sorted_list = fruits.copy()
sorted_list.sort(reverse = True)
print(sorted_list)

numbers = [2,5,7,9,12,333,5,5,5,5,99999,11223,2]
numbers.sort()
print(numbers)"""