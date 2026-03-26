#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def add(x,y):
  return x + ", " + y

final = reduce(add, countries)
final = final.replace("Iceland", "and Iceland")
print(f"{final} are north European Countries")