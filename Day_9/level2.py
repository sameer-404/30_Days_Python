#Write a code which gives grade to students according to theirs scores:
"""90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
"""

score = int(input("Enter your score: "))

if score > 90:
  print("Score: A")
elif 80 < score < 89:
  print("Score: B")
elif 70 < score < 79:
  print("Score: C")
elif 60 < score < 69:
  print("Score: D")
else:
  print("Score: F")


