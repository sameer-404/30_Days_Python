#Flatten the following list of lists of lists to a one dimensional list :



"""output
[1, 2, 3, 4, 5, 6, 7, 8, 9]"""

def flatten(list_of_lists):
    return [i for sublist in list_of_lists for i in sublist]

result = flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]