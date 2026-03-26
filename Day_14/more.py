#Use filter to filter out countries containing six letters and more in the country list
countries = [
    'Albania', 'Bolivia', 'Canada', 'Denmark', 'Ethiopia',
    'Finland', 'Germany', 'Hungary', 'India', 'Japan',
    'Kenya', 'Latvia', 'Mexico', 'Nigeria', 'Norway',
    'Pakistan', 'Qatar', 'Russia', 'Sweden', 'Tanzania',
    'Uganda', 'Vietnam', 'Zambia', 'Brazil', 'Iceland',
    'Ireland', 'New Zealand', 'Switzerland', 'Thailand', 'Finland'
]

def six_or_more(country):
    if len(country) >= 6:
        return True
    else:
        return False
    
six_or_more_countries = list(filter(six_or_more, countries))
print(six_or_more_countries)