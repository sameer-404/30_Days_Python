#Day: 8 - Dictionaries

#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#creating a dictionary:
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
    }"""

#The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.
"""print(len(person))"""


#Accessing Dictionary Items
#We can access Dictionary items by referring to its key name.
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
    }"""

#For example:
"""print(person.get("first_name"))"""
"""first_name = person.get("first_name")
print(first_name)

address_zip = person.get("address").get("zipcode") #To get value of dictionary inside a dictionary
print(address_zip)"""

#Adding Items to a Dictionary
#We can add new key and value pairs to a dictionary
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

person["date"] = "never"
print(person)
#U aint never getting the date bro gave up!

#Alternate method:
person['skills'].append("C")
print(person["skills"])"""

#Modifying Items in a Dictionary
"""
person = {
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
person['first_name'] = 'Sameer'
person["age"] = 21
print(person.get("age"))
print(person.get("first_name"))"""

#Checking Keys in a dictionary:
#We use the in operator to check if a key exist in a dictionary

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

print("first_name" in person) #True as that key exist
print("idk" in person) #there's no such key
"""

#Removing Key and Value Pairs from a Dictionary
#pop(key): removes the item with the specified key name:
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
person.pop("first_name")
print(person.get("first_name"))

person.popitem()
print(person.get("address"))
del person['is_married']  #Removes the is_married item from the dictionary"""

#Both of them throw none as output cause get() method have default value none


#Changing Dictionary to a List of Items
#The items() method changes dictionary to a list of tuples.
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
print(person.items()) #Changes a dictionary into a list of tuples"""


#Clearing a Dictionary
#If we don't want the items in a dictionary we can clear them using clear() method
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

person.clear()
print(person["first_name"])"""

#Copy a Dictionary
#We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
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

Asabeneh = person.copy()
person.clear()
print(person)
print(Asabeneh)

#del dictionary using del() keyword
del person
print(person)"""

#Getting Dictionary Keys as a List
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
#The keys() method gives us all the keys of a a dictionary as a list.
#For example
keys = person.keys()
print(keys)

#Getting Dictionary Values as a List
#The values method gives us all the values of a a dictionary as a list.

values = person.values()
print(values)"""