#Find the middle country(ies) in the countries list

countries = [
    "China", "Sweden", "Austria", "Malaysia", "Honduras", "Fiji", "Puerto Rico",
    "Mali", "United Arab Emirates", "Canada", "United States", "Japan", "South Korea",
    "Russia", "Finland", "Greece", "Italy", "Australia", "Indonesia", "Belgium",
    "Maldives", "Brazil", "Peru", "Libya", "United Kingdom", "Argentina", "Ethiopia",
    "Egypt", "Singapore", "Mexico"
]

length = len(countries)
if length//2 == 1:
  print(f"The middle country is : {countries[length//2]}")
else:
  middle_country1 = countries[length//2]
  middle_country2 = countries[(length//2)-1]
  print(f"The middle countries are: {middle_country2} and {middle_country1}")