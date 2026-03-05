it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Find the length of the set it_companies
length = len(it_companies)
print(f"The length of it companies is: {length}")

#Add 'Twitter' to it_companies
it_companies.update(["Twitter"])
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(["Iners", "Anthropic", "deepseek"])
print(it_companies)

#Remove one of the companies from the set it_companies
removed = it_companies.pop()
print(it_companies)
print(removed)

#What is the difference between remove and discard
it_companies.remove("Facebook")
print(it_companies)
#when we assign non existing item in remove - it raises keyerror
#it_companies.remove(99)

#but discard removes, if something is not found it doesnt do nothing and doesnt even raise errors
it_companies.discard("Iners")
print(it_companies)
it_companies.discard(99) #No errors here
print(it_companies)