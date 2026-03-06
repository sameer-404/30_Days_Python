#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
  "first_name" : "Sameer",
  "last_name" : "Yogi",
  "gender" : "Male",
  "marital_status" : False,
  "skills" : ["Python","C", "Java", "CSS", "HTML", "JS"],
  "country" : "Nepal",
  "city" : "Kathmandu",
  "address" : "Chandragiri"
}

#Get the length of the student dictionary
length = len(student)
print(f"The length of student dictionary is: {length}")

#Get the value of skills and check the data type, it should be a list
skills = student.get("skills")
print(skills)
print(type(skills))

#Modify the skills values by adding one or two skills
student["skills"].append("C++")
student["skills"].append("C#")
print(student["skills"])

#Get the dictionary keys as a list
key_list = student.keys()
print(key_list)

#Get the dictionary values as a list
values_list = student.values()
print(values_list)

#Change the dictionary to a list of tuples using items() method
tuple_dict = student.items()
print(tuple_dict)

#Delete one of the items in the dictionary
student.pop("country")
#print(student["country"])

#Delete one of the dictionaries
del student

try:
    print(student)
except NameError:
    print("student dictionary successfully deleted")