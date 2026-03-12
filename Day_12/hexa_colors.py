#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def hexa_colors(number):
  options = ["a", "b", "c", "d", "e", "f", "0", "1", "2" ,"3" ,"4" ,"5", "6", "7", "8", "9"]
  colors = []

  for each in range(number):
    color_code = ""
    for i in range(6):
      color_code += random.choice(options)
    colors.append("#" + color_code)

  return colors


number = int(input("Enter how many times you want hexa codes: "))
result = hexa_colors(number)
print(result)