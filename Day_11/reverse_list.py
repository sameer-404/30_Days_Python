#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
"""
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
"""

def reverse_list(my_list):
    reversed_list = []
    for each in range(len(my_list)-1, -1, -1):
        reversed_list.append(my_list[each])  # append actual item not index!
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))  # ['C', 'B', 'A']