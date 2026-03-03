#Sort the list using sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#Slice out the first 3 companies from the list
sliced_companies = it_companies[0:3]
print(sliced_companies)

#Slice out the last 3 companies from the list
last_sliced = it_companies[-3:]
print(last_sliced)
