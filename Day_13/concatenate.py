#Change the following list of lists to a list of concatenated strings:

"""output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']"""

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [first + ' ' + last for sublist in names for first, last in sublist]

print(result)