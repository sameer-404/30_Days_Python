#Declare an empty list

my_list = []
fruits = ["apple", "banana", "carrot", "kiwi", "pomegranate"]
print(f"Length of first string is: {len(my_list)}")
print(f"Length of Second List is: {len(fruits)}")

#Get the first item, the middle item and the last item of the list
first_item = fruits[0]
last_item = fruits[-1]
middle_index = int(((len(fruits)+1)/2)-1)
middle_item = fruits[middle_index]
print(f"First item is: {first_item}")
print(f"Middle itm is: {middle_item}")
print(f"Last item is: {last_item}")

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Sameer Yogi", 21, 5.7, False, "396_Piedmont_Ave_NE"]
print(mixed_data_types)