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

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)