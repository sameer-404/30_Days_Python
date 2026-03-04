#Create an empty tuple
empty = tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Sameer", "Saurav", "Samrat", "Pragig")
sisters = ("Sampada", "Pranita")

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

#How many siblings do you have?
total_siblings = len(siblings)
print(f"Total number of siblings are: {total_siblings}")

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
print(siblings)
siblings.append("Tika")
siblings.append("Dhan Nath")
print(siblings)
family_members = tuple(siblings)
print(family_members)