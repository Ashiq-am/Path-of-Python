s = [{"name": "John", "age": 18}, {"name": "Jane", "age": 20}]

#Using List Comprehension to extract the 'name' of
#each student from the list of dictionaries
n = [student["name"] for student in s]
print(n)