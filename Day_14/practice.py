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


#Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

#Key concept:
#Functions in Python can be passed as arguments, stored in variables, and used just like other objects.
