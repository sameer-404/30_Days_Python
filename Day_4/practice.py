#check = "Hello World"
#print(len(check))

"""
first_name = "Sameer"
space = " "
last_name = "Yogi"
full_name = first_name + space + last_name
print(full_name)
print(len(full_name))
"""
#print("I hope everyone is enjoying the Python Challenge. \nAre you?")

"""
print("I hope every one is enjoying the Python Challenge. \nAre you?")
print("Days\tTopics\tExercises")
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("Day 3\t5\t23")
print("This is a backslash symbol (\)")
print("In every programming language it starts with 'Hello, World!'")
"""

"""a = 4
b = 3 
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')"""

"""language = "Python"
first_letter = language[0]
second_letter = language[1]
last_index = len(language) - 1 
last_letter = language[last_index]
print(first_letter)
print(second_letter)
print(last_letter)"""

#reverse indexing:
"""language  = "Python"
last_letter = language[-1]
second_last = language[-2]
print(last_letter)
print(second_last)"""

#String Slicing:
"""language = "Python"
first_three = language[0:3] # starts with 0 index and goes to 3 but 3 is not included, so 0,1,2
print(first_three)
#last_three = language[3:6] #starts with 3 and upto 6 , 6 not included(3,4,5)
print(last_three)
"""
#Alternate way for last three:
"""last_three = language[-3:] #That means -3 to 0 so 3 last numbers
print(last_three)
last_three = language[3:]
print(last_three)"""

"""
#reversing a string:
greetings = "Namaste!"
print(greetings[::-1])
"""

"""#Skip slicing:
language = "Python"
pto = language[0:6:2] # or we can use [::2]
print(pto)"""

"""
# String Methods:
sentence = "There are a number of reasons you may need a block of text and when you do, a random paragraph can be the perfect solution. If you happen to be a web designer and you need some random text to show in your layout, a random paragraph can be an excellent way to do this. If you're a programmer and you need random text to test the program, using these paragraphs can be the perfect way to do this. Anyone who's in search of realistic text for a project can use one or more of these random paragraphs to fill their need."
sentence = sentence.lower()
print(sentence.count("i"))

#specially helpful when u want to count some words, like the
print(sentence.count("the"))

#we can also bound this whenever we want , like from which index to what index
print(sentence.count("a",0,50))"""