#Day 11: Functions

#what is a function?
#A function is a reusable block of code or programming statements designed to perform a certain task.
#To define a function , python provides the def keyword.
#The following is the syntax for defining a function.

#Declaring and calling a function
#When we make a function, we call it declaring a function.
#When we start using it , we call it calling a function.

#For example:
"""def generate_full_name():
  first_name = "Sameer"
  last_name = "Yogi"
  space = " "
  full_name = first_name + space + last_name
  print(full_name)

generate_full_name()
"""
#Another example:
"""def add_two_numbers():
  num1 = int(input("Enter your number: "))
  num2 = int(input("Enter second number: "))
  sum = num1 + num2
  print(sum)

add_two_numbers()"""


#Function returning a value - part1:
#Functions return values using the return statement
#If a function has no return statement, it returns none

#Let's rewrite the above functions using return
"""def generate_full_name():
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last_name: ")
  fullname = first_name + " " + last_name
  return fullname

full = generate_full_name()
print(f"Fullname: {full}")"""

"""def add_two_numbers():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  sum = num1 + num2
  return sum

sum = add_two_numbers()
print(f"Sum: {sum}")"""


#Functions with parameters:
#In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as parameters

#Single parameter:
#If our function takes a parameter we should call our function with an argument

#For example:
"""def greetings(name):
  message = "What's good?" + " " + name
  return message

print(greetings("Sameer")) """

"""def square(num):
  return num * num

result = square(5)
print(f"Squared: {result}")"""

"""def sum_of_numbers(n):
  total = 0
  for i in range(n+1):
    total += i
  return total

result = sum_of_numbers(5)
print(f"Sum: {result}")"""

#two parameters:
#A function may or may not have parameter or parameters.
#A function may also have two or more parameters.
#If our function takes parameters we should call it with arguments.
#For example:

"""def generate_full_name(first_name, last_name):
  full_name = first_name + " " + last_name
  return full_name

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = generate_full_name(first_name, last_name)
print(f"Full name: {full_name}")
"""

"""def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

birth_year = int(input("When was u born: "))
current_year = int(input("What year is this: "))
age = calculate_age(current_year, birth_year)
print(f'Your age is : {age}')"""

#Passing arguments with key and value:
#If we pass the argument with key and value , the order of the arguments doesn't matter
#hardcoding the arguments basically
#For example:

"""def add_two_numbers(num1, num2):
  sum = num1 + num2
  return sum

print(add_two_numbers(num2=5, num1=2))"""
#the order doesnt matter!


#Function returning a value - part2:
#If we dont return a value with a function, then our function is returning None by default.
#To return a value with a function we use the keyword return followed by the variables we are returning.
#We can return any kind of data types from a function
"""
def print_full_name(firstname, lastname):
  space = " "
  full_name = firstname + space + lastname
  return full_name

print(print_full_name(firstname="Sameer", lastname="Yogi"))"""

#Returning a number:
"""def add_two_numbers(num1, num2):
  total = num1 + num2
  return total

print(add_two_numbers(2,3))
"""
"""
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

print("Age:",calculate_age(2026,2004))"""

#returning a boolean:
"""def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False
  
print(is_even(10))
print(is_even(11))"""

#Returning a list:
"""def find_even_numbers(n):
  evens = []
  for i in range(n+1):
    if i % 2 == 0:
      evens.append(i)
  return evens
  
print(find_even_numbers(10))"""

#Functions with default parameters:
#Sometimes we pass default values to parameters, when we invoke the function.
#If we dont pass arguments when calling the function, their defaukt values will be used
#so if the user doesnt provide any info, default is used and if user puts arguments then default is not used!
"""def greeting(name = "Sameer"):
  message = name + ", welcome!"
  return message

print(greeting())
print(greeting("Saurav"))"""

"""def calculate_age(birth_year, current_age = 2026):
  age = current_age - birth_year
  return age

print(f"Age: {calculate_age(2002, 2025)}")

print(f"Age: {calculate_age(2002)}")
"""


#Arbitraty number of arguments:
#if we dont know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

"""def sum_all_nums(*nums):
  total = 0
  for num in nums:
    total += num
  return total
print(sum_all_nums(2,3,4,5))""" #Important



#Default and arbitrary number of parameters in function:
"""def generate_groups(team, *args):
  print(team)
  for i in args:
    print(i)

generate_groups("Team-1", "Sameer", "Saurav", "David")"""

"""#Dictionary unpacking
#You can call a function which has named arguments using a dictionary with matching key names.
#You do so using **

#Define a function that takes two arguments: "name" and "location"
def greet(name, location):
  #print a greeting message using the provided argument
  print("Hi there", name , "how is the weather in" , location)

#call the function usinf keyword arguments
#greet(name="Sameer", location="Atlanta")
#Output:
#Hi there Sameer how is the weather in Atlanta

#create a dictionary with kets matchinf the function's parameters names
my_dict = {"name": "Sameer", 
           "location": "Atlanta"}

#Call the function usinf dictionary unpacking
greet(**my_dict)
#It works the same as using keyword arguments
#the ** operator unpacks the dictionary , passing its key-value pairs
#as keyword arguments to the function
#Output: Same"""



#Function as a parameter of another function:
#You can pass function around as parameters
"""def square_number(n):
  return n ** n
def do_something(f,x):
  return f(x)
print(do_something(square_number,3))"""