#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
splitted_list = sentence.split()
print(splitted_list)
splitted_set = set(splitted_list)
unique_words = len(splitted_set)
print(splitted_set)
print(f"Number of unique words: {unique_words  }")