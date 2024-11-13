import json
#Parsing the JSON String
string = '[{"name" : "Harsha", "subject" : "Physics" , "Code" : "java" }]'
list1 = json.loads(string)

#Converting into the list
another_list = [ i for i in list1[0]]

#Extracting the keys in the dictionary
print(type(string))
print(another_list)
print(type(another_list))
