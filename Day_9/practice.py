#Conditionals:
#By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

#Conditional execution: a block of one or more statements will be executed if a certain expression is true
#Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.

#If Condition:
#In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

#For example:
"""a = 5
if a > 0:
  print(f"{a} is positive")"""

#As you can see in the example above, 3 is greater than 0. The condition was true and the block code was executed. However, if the condition is false, we do not see the result. In order to see the result of the falsy condition, we should have another block, which is going to be else.

#If Else:
#If condition is true the first block will be executed, if not the else condition will run.

"""a = -5
if a > 5:
  print(f"{a} is positive")
else:
  print(f"{a} is negative")
"""
#The condition above proves false, therefore the else block was executed. How about if our condition is more than two? We could use elif.
"""
a = 0
if a > 0:
  print(f"{a} is positive")
elif a < 0:
  print(f"{a} is negative")
else:
  print(f"{a} is zero")"""

#Short hand:
"""a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed"""

#Nested Conditions
#Conditions can be nested
"""a = 0
if a > 0:
  if a % 2 == 0:
    print(f"{a} is positive and even")
  else:
    print(f"{a} is positive")
elif a < 0:
  print(f"{a} is negative")
else:
  print(f"{a} is zero")"""

#We can avoid writing nested condition by using logical operator and.
#For example:
"""a = 2
if a > 0 and a % 2 == 0:
  print(f"{a} is positive and even")
elif a > 0 and a % 2 != 0:
  print(f"{a} is a positive integer")
elif a == 0:
  print(f"{a} is zero")
else:
  print(f"{a} is negative")"""

#If and Or Logical Operators
"""user = "sameer"
user_level = 3
if user == "sameer" or user_level == 2:
  print("Access granted!")
else:
  print("Access denied")"""

#one condition has to be true!