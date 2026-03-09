#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(uncapitalized):
    capital = []
    for each in uncapitalized:  # loop directly!
        capital.append(each.upper())
    return capital


capitalized = capitalize_list_items(["hello", "world"])
print(capitalized)