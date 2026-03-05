age = [22, 19, 24, 25, 26, 24, 25, 24]
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
len_list = len(age)
age = set(age)
print(age)
len_set = len(age)
print(f"The length of list: {len_list} and length of set: {len_set}")


