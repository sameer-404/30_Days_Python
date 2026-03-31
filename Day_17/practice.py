#Exception Handling:
"""
try:
  print(10 + "5")
except:
  print("Something went wrong!")
"""

"In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, except, will be executed."

"""
try:
    name = input("Enter your name: ")
    year = input("What year were you born: ")
    age = 2026 - year
    print(f"You are {name}, and you are {year} old!")
except:
   print("Something went wrong!")"""


#In the above example, the exception block will run and we donot know what exactly caused the problem. To analyse the problem, we can use the different error types with except.
"""
try:
  name = input("Enter your name: ")
  year = input("What year were you born in: ")
  age = 2026 - int(year)
  print(f"You are {name}, and you are {age} years old!")
except TypeError:
  print("Type error occured!")
except ValueError:
  print("Value Error Occured!")
except ZeroDivisionError:
  print("Zero Division Error Occured!")
else:
  print("No error occured, everything ran fine!")
finally:
  print("Finally we are out of the program and it always run!")"""


#Packing and Unpacking Arguments in Python:

#Unpacking Lists:
"""def sum_of_five_nums(a,b,c,d,e):
  return a+b+c+d+e

lst = [1,2,3,4,5]"""
#print(sum_of_five_nums(lst)) #Will raise an typeerror as it takes 5 arguments doesn't matter if that lists have 5 numbers or not!

#We can use unpacking by using *lst
"""print(sum_of_five_nums(*lst))"""

#We can also use unpacking in the range built in function that expects a start and an end
"""numbers = range(2,7)

print(list(numbers)) #[2,3,4,5,6]
args = [2,7]
#Unpacking!
numbers = range(*args)
print(numbers)"""

#A list of tuple can also be unpacked like this:
"""countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin , sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1,2,3,4,5,6,7,8,9]
one, *middle, last = numbers
print(one, middle, last)"""

#Unpacking Dictionaries:

"""def unpacking_person_info(name, country, city, age):
  return f"{name} lives in {country}, {city}. He is {age} year old."
dct = {"name": "Sameer",
       "country": "Nepal",
       "city": "Kathmandu",
       "age": 21}
print(unpacking_person_info(**dct))
"""

#Packing:
#Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function

#Packing Lists:
"""def sum_all(*args):
  s = 0
  for i in args:
    s += i
  return s
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6,7))"""

#Packing Dictionaries:

"""def packing_person_info(**kwargs):
  #check the type of kwargs and it is a dict type
  #print(type(kwargs))
  #printing dictionary items
  for key in kwargs:
    print(f"{key} = {kwargs[key]}")
  return kwargs

print(packing_person_info(name= "Sameer",
                          country = "Nepal", 
                          city = "Kathmandu", 
                          age = "21"))
"""


#Spreading in Python
#Like in javascript, spreading is possible in Python.
#For example:

"""lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)
#[1,2,3,4,5,6,7]

country_lst_one = ["Finland", "Sweden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)
#["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
"""


#Enumerate:
#If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list

"""countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for index, i in enumerate(countries):
  if i == "Finland":
    print(f"The country {i} has been found at index {index}")"""

#Zip:
#Sometimes we worry like to combine lists when looping through them.
#For example:

"""fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["tomato", "potato", "cabbage", "onion", "carrot"]
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
  fruits_and_veges.append({"fruits": f, "veg": v})

print(fruits_and_veges)"""

