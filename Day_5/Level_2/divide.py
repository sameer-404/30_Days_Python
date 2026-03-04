#Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = [
    "China", "Sweden", "Austria", "Malaysia", "Honduras", "Fiji", "Puerto Rico",
    "Mali", "United Arab Emirates", "Canada", "United States", "Japan", "South Korea",
    "Russia", "Finland", "Greece", "Italy", "Australia", "Indonesia", "Belgium",
    "Maldives", "Brazil", "Peru", "Libya", "United Kingdom", "Argentina", "Ethiopia",
    "Egypt", "Singapore" , "Mexico"
]
countries.sort()

length = len(countries)

if length % 2 == 1:  # % 2 checks for remainder
    print("It's odd!")
    middle_item = (length // 2) - 1
    print(f"Middle country is: {middle_item}")
    print(f"The list is : {countries[0:middle_item]}")
    print("and")
    print(f"{countries[middle_item:]}")
else:
    print("It's even!")
    middle_item2 = (length //2)
    print(f"The list is : {countries[0:middle_item2]}")
    print("and")
    print(f"{countries[middle_item2:]}")