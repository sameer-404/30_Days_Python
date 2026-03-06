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

person["date"] = "never"
print(person)
#U aint never getting the date bro gave up!
