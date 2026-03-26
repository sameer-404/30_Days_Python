#Dqy - 14: Higher Order Function!

#Higher Order Functions

#In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:
"""
A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
"""

#In this section, we will cover:
#Handling functions as parameters
#Returning functions as return value from another functions
#Using Python closures and decorators


#Function as a Parameter:
"""def double(x):
    return x * 2

def triple(x):
    return x * 3

def apply(f, number):    # higher-order function
    return f(number)


print(apply(double, 5))  # 10
print(apply(triple, 5))  # 15"""
"""def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3"""

#Python Closures:
#Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

#for example:
"""def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add          # returns add function with ten "saved inside"

closure_result = add_ten()  # closure_result is now the add function
print(closure_result(5))    # 15  →  5 + 10
print(closure_result(10))   # 20  →  10 + 10"""



#Python Decorators
#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

#Creating Decorators
#To create a decorator function, we need an outer function with an inner wrapper function.
"""
def shout(func):
    def wrapper():
        print("GET READY!")
        func()
        print("DONE!")
    return wrapper

@shout
def say_name():
    print("My name is Sameer")

say_name()"""


#Applying Multiple Decorators to a Single Function


#Bro code:
#Decorators = A function that extends the behavior of another function w/o modifying the base function
#pass the base function as an argument to the decorator

"""def add_sprinkles(func):
  def wrapper(*args, **kwargs):
    print("you added sprinkles!")
    func(*args, **kwargs)
  return wrapper

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("You added fudge!")
    func(*args, **kwargs)
  return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
  print(f"Here is your {flavor} icecream!!!")

get_ice_cream("vanilla")


"""


#Built-in Higher Order Functions

#Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduc

#python - map function:
#Map function - map(function, iterable)
#returns an iterator that applied function to every item of iterable\
"""
def make_even(num):
    if num % 2 == 1:
        return num -1
    else:
        return num

x = [551, 641, 122, 435, 223, 234, 343, 561, 115, 552, 111, 679, 101]

#Old method:
""""""y = []
for num in x:
    y.append(make_even(num))

print(y)"""
"""
#Map function:
y = list(map(make_even, x))
print(y)"""


#filter function = filter(function, iterable)
#returns items from iterable based on some criteria

#for examples:
#Let's filter out only even numbers:
"""numbers = [1,2,3,4,5,6,7,8,9] #iterable

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False
  
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

#It can also be done in dictionary for example:
#We want to find a room which has more than 2 bedrooms and less than $1600


avail_units = {
    '101': {
        'bedrooms': 3,
        'bathrooms': 2,
        'price': 1625
    },
    '215': {
        'bedrooms': 2,
        'bathrooms': 2,
        'price': 1550
    },
    '231': {
        'bedrooms': 1,
        'bathrooms': 1,
        'price': 1400
    },
    '431': {
        'bedrooms': 2,
        'bathrooms': 1,
        'price': 1500
    },
    '422': {
        'bedrooms': 2,
        'bathrooms': 1,
        'price': 1300
    },
    '310': {
        'bedrooms': 3,
        'bathrooms': 2,
        'price': 1800
    },
    '512': {
        'bedrooms': 1,
        'bathrooms': 1,
        'price': 1100
    }
}

def my_filter(unit_num):
  if avail_units[unit_num]["price"] < 1900 and avail_units[unit_num]["bedrooms"] > 2:
    return True
  else:
    return False
  
result = list(filter(my_filter, avail_units))
print(result)"""


#Python reduce Function:
#The reduce function is defined in the fucntion module and we should import it from this module. Like map and filter it takes two paramaters , a function and an iterable. However, it does not return another iterable, instead it returns a single value.

#for example:
"""from functools import reduce  

numbers_str = ["1", "2", "3", "4", "5", "6"]

def add_two_nums(x,y):
  return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)"""

"""
numbers_str = ["1", "2", "3", "4", "5", "6"]
```
```
["1", "2", "3", "4", "5", "6"]
  ↓    ↓
add(1, 2) = 3
       ↓    ↓
    add(3, 3) = 6
           ↓    ↓
        add(6, 4) = 10
               ↓    ↓
           add(10, 5) = 15
                   ↓    ↓
               add(15, 6) = 21 ← final answer
"""