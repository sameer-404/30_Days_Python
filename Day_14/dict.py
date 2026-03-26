#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


countries = [
    'Albania', 'Bolivia', 'Canada', 'Denmark', 'Ethiopia',
    'Finland', 'Germany', 'Hungary', 'India', 'Japan',
    'Kenya', 'Latvia', 'Mexico', 'Nigeria', 'Norway',
    'Pakistan', 'Qatar', 'Russia', 'Sweden', 'Tanzania',
    'Uganda', 'Vietnam', 'Zambia', 'Brazil', 'Iceland',
    'Ireland', 'New Zealand', 'Switzerland', 'Thailand', 'Finland',
    'Kazakhstan', 'Uzbekistan', 'Afghanistan', 'Romania', 'Croatia'
]

def count_countries_by_letter(countries):
    result = {}
    for country in countries:
        letter = country[0]
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

print(count_countries_by_letter(countries))
