# Python code to initialize a dictionary
# with only keys from a list

# List of keys
Student = ["Paras", "Jain", "Cyware"]

# using fromkeys() method
StudentDict = dict.fromkeys(Student, None)

# printing dictionary
print(StudentDict)
