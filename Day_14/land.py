#Use filter to filter out countries containing 'land'.

countries = [
    'Albania', 'Bolivia', 'Canada', 'Denmark', 'Ethiopia',
    'Finland', 'Germany', 'Hungary', 'India', 'Japan',
    'Kenya', 'Latvia', 'Mexico', 'Nigeria', 'Norway',
    'Pakistan', 'Qatar', 'Russia', 'Sweden', 'Tanzania',
    'Uganda', 'Vietnam', 'Zambia', 'Brazil', 'Iceland',
    'Ireland', 'New Zealand', 'Switzerland', 'Thailand', 'Finland'
]

def has_land(country):
    if "land" in country:
        return True
    else:
        return False
    
land_countries = list(filter(has_land, countries))
print(land_countries)