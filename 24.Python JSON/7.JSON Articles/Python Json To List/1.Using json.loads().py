import json
#taking a string
string = "[1,2,3,4]"

#Passing the string into the json.loads() method
array = json.loads(string)

print(type(string))
print(array[0])
print(type(array))
