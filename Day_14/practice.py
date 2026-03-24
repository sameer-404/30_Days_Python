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

