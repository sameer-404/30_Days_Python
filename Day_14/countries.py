#Use for loop to print each country in the countries list.


countries = [
    'Albania', 'Bolivia', 'Canada', 'Denmark', 'Ethiopia',
    'Finland', 'Germany', 'Hungary', 'India', 'Japan',
    'Kenya', 'Latvia', 'Mexico', 'Nigeria', 'Norway',
    'Pakistan', 'Qatar', 'Russia', 'Sweden', 'Tanzania',
    'Uganda', 'Vietnam', 'Zambia', 'Brazil', 'China'
]

"""for country in countries:
  print(country)"""

#Use map to create a new list by changing each country to uppercase in the countries list

def uppercase(country):
  return country.upper()

upper_cased_countries = list(map(uppercase, countries ))
print(upper_cased_countries)