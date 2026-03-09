#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celcius_to_fahrenheit(celcius):
  F = (celcius*(9/5)) + 32
  return F

C = int(input("Enter your temp in degree celcius: "))
result = convert_celcius_to_fahrenheit(C)
print(f"Converted temperature: {result}")
