#Day 10:
#Loops:
#Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:
#1.while loop
#2.for loop

#While loop:
# It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

#For example:
"""count = 0
while count < 5:
  print(count)
  count += 1"""

#In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.
"""count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
"""
#The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

#Break and Continue - Part 1
#Break: We use break when we like to get out of or stop the loop.

#For example:
"""count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
"""
#Prints, 0,1,2

#Continue: With the continue statement we can skip the current iteration, and continue with the next:
#for example:
"""count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1"""

#For Loop
#A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#For example:
"""numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
"""
#using for loop in string:
"""python = "Python"

for word in python:
    print(word)

#Or
for i in range(len(python)):
    print(python[i])"""

#Using for loop in tuple:
"""
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)"""

#For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
"""person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
  print(key)

for key, value in person.items():
    print(f"{key} : {value}") # this way we get both keys and values printed out"""


#Using For Loop in set
"""it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)"""

#Break and Continue - Part 2
#Short reminder: Break: We use break when we want to stop our loop before it is completed.
"""numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
"""

#Continue: We use continue when we want to skip some of the steps in the iteration of the loop.
"""numbers = (0, 1, 2, 3, 4, 5)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')"""

#The Range Function:
#The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
#syntax:
# for iterator in range(start, end, step):

#For example:
"""for number in range(11):
    print(number) """

#Nested For Loop:
#We can write loops inside a loop.
#For example:
"""person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
  if key == "skills":
    for skill in person["skills"]:
      print(skill)""" #This was important

#For Else
#If we want to execute some message when the loop ends, we use else.
"""for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)"""

#Pass
#In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
"""for number in range(6):
    pass"""
#Does nothing just a place holder