#Use for to print each name in the names list.
names = [
    'Alice', 'Bob', 'Charlie', 'Diana', 'Edward',
    'Fatima', 'George', 'Hannah', 'Ivan', 'Julia',
    'Kevin', 'Laura', 'Michael', 'Nina', 'Omar',
    'Paula', 'Quinn', 'Rachel', 'Samuel', 'Tina'
]

#Use map to change each name to uppercase in the names list

def upper(name):
  return name.upper()

upper_names = list(map(upper, names))
print(upper_names)