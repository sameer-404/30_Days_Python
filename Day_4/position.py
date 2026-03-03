#Use index to determine the position of the first occurrence of C in Coding For All.
sentence = "Coding For All"
print(sentence.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(sentence.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
another_sentence = "Coding For All People"
print(another_sentence.rfind("l"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
paragraph = "You cannot end a sentence with because because because is a conjunction"
print(paragraph.index("because"))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(paragraph.rindex("because"))

