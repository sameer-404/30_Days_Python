#Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = [
    "China", "Sweden", "Austria", "Malaysia", "Honduras", "Fiji", "Puerto Rico",
    "Mali", "United Arab Emirates", "Canada", "United States", "Japan", "South Korea",
    "Russia", "Finland", "Greece", "Italy", "Australia", "Indonesia", "Belgium",
    "Maldives", "Brazil", "Peru", "Libya", "United Kingdom", "Argentina", "Ethiopia",
    "Egypt", "Singapore", "Mexico"
]

length = len(countries)

if length//2 == 1:
  middle_county_index = length//2
  print(f"The first halves countries are: {countries[:middle_county_index]}")
