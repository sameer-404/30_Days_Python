#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']


full_stack = front_end + back_end

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
#First find the index of Redux

index_of_Redux = full_stack.index("Redux")
print(index_of_Redux)

full_stack.insert(index_of_Redux+1, "SQL")
full_stack.insert(index_of_Redux+1, "Python")
print(full_stack)