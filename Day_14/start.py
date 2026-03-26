#Use filter to filter out countries starting with an 'E'
countries = [
    'Albania', 'Bolivia', 'Canada', 'Denmark', 'Ethiopia',
    'Finland', 'Germany', 'Hungary', 'India', 'Japan',
    'Kenya', 'Latvia', 'Mexico', 'Nigeria', 'Norway',
    'Pakistan', 'Qatar', 'Russia', 'Sweden', 'Tanzania',
    'Uganda', 'Vietnam', 'Zambia', 'Brazil', 'Iceland',
    'Ireland', 'New Zealand', 'Switzerland', 'Thailand', 'Finland'
]

def start_E(country):
  if country.startswith("E") or country.startswith("e"):
    return True
  else:
    return False
  
country_starting_E = list(filter(start_E, countries))
print(country_starting_E)