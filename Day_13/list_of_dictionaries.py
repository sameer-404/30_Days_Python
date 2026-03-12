#Change the following list to a list of dictionaries:
"""output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [{'country': country.upper(), 'city': capital.upper()} 
          for sublist in countries 
          for country, capital in sublist]

print(result)