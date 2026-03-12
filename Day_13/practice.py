#Day 13: List Comprehension!

#List Comprehension:
#List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.
# syntax
# [expression for i in iterable if condition]

#For example:


#Example:1
#For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:
#First method:
"""language = "Python"
lst = list(language)
print(lst)"""

#Second method:
"""language = "python"
lst = [i for i in language]
print(lst)
"""

#Example: 2
#For instance if you want to generate a list of numbers
"""numbers = [i for i in range(5)]
print(numbers)

squares = [i*i for i in range(5)]
print(squares)

## It is also possible to make a list of tuples
number = [(i,i*i) for i in range(5)]
print(number)"""



#Example: 3
#List comprehension can be combined with if expression
"""
#Generating even numbers:
even_numbers = [i for i in range(21) if (i % 2 == 0)]
print(even_numbers)

## Generating odd numbers
odd_numbers = [i for i in range(22) if (i %2 != 0)]
print(odd_numbers)

## Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
even_positive_numbers = [i for i in numbers if i%2 ==0 and i > 0]
print(even_positive_numbers)"""

#Lambda Function:
#Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

#Creating a Lambda Function
#To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

## syntax
"""x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))"""

#For example:
"""def add_two_nums(a,b):
  return a + b

print(add_two_nums(3,5))
"""
## Lets change the above function to a lambda function
"""add_two_nums = lambda a, b: a + b
print(add_two_nums(3,5))
"""

## Self invoking lambda function
"""print((lambda a,b : a+b)(2,5))

square = lambda x : x ** 2
print(square(3))"""


## Multiple variables
"""multiple_variable = lambda a, b, c : a ** 2 - 3 * b + 4 * c
print(multiple_variable(5,5,3))"""



#Using lambda inside another function:
def power(x):
    return lambda n : x ** n

cube = power(2)(3)
print(cube)

"Full code for this above code:"
"""
# Define the power function
def power(x):
    return lambda n: x ** n

# Step 1: Call power(2) to get a function
f = power(2)  # f is now: lambda n: 2 ** n

# Step 2: Call the returned lambda with an argument
cube = f(3)    # computes 2 ** 3 = 8

print(cube)"""