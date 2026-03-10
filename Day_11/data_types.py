#Write a function which checks if all the items of the list are of the same data type.

def check_data(fruits):
    for i in range(len(fruits) - 1):
        if type(fruits[i]) != type(fruits[i+1]):
            print("They are not same data types!")
            return
    print("They are all of same data types!")

fruits = ["banana", "kiwi", "pomegranate", "cabbage", 2]
check_data(fruits)


#Alternate method using sets:
"""def check_data(fruits):
    types = set()
    for i in fruits:
        types.add(type(i))
    
    if len(types) == 1:
        print("They are all of same data types!")
    else:
        print("They are not same data types!")

fruits = ["banana", "kiwi", "pomegranate", "cabbage"]
check_data(fruits)"""

#set one was easier!