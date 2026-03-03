#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find("because")
print(start)
end = sentence.rfind("because")
print(end)
last_occurance = sentence.rfind("because")
#but word because itself is 7 characters so index of end of because = end+7
end = int(end) + 7
actual_end = end
print(actual_end)
extracted = print(sentence[start:actual_end])
print(last_occurance)
