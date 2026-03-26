#Use filter to filter out countries having exactly six characters.
countries = [
    'Albania', 'Bolivia', 'Canada', 'Denmark', 'Ethiopia',
    'Finland', 'Germany', 'Hungary', 'India', 'Japan',
    'Kenya', 'Latvia', 'Mexico', 'Nigeria', 'Norway',
    'Pakistan', 'Qatar', 'Russia', 'Sweden', 'Tanzania',
    'Uganda', 'Vietnam', 'Zambia', 'Brazil', 'Iceland',
    'Ireland', 'New Zealand', 'Switzerland', 'Thailand', 'Finland'
]

def is_six(country):
  if len(country) == 6:
    return True
  else:
    return False
  
six_char_countries = list(filter(is_six, countries))
print(six_char_countries)