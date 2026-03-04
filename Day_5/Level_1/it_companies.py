#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(f"Number of companies: {len(it_companies)}")

#Print the first, middle and last company
first = it_companies[0]
last = it_companies[-1]
middle_index = int(((len(it_companies)+1)/2)-1)
middle = it_companies[middle_index]
print(f"First Company: {first}")
print(f"Last Company: {last}")
print(f"Middle Company: {middle}")

#Print the list after modifying one of the companies
it_companies[2] = "Microhard"
print(it_companies)

#Add an IT company to it_companies
it_companies.append("Iners_Tech")

middle_index = len(it_companies) // 2

#Insert an IT company in the middle of the companies list
it_companies.insert(middle_index, "New_Guy!!!!")

print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
print("#; ".join(it_companies))

#Check if a certain company exists in the it_companies list.
does_exist = "Apple" in it_companies
print(does_exist)