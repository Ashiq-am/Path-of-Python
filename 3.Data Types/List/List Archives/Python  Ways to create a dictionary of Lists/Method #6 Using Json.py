#importing json
import json

#Initialisation of list
lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]

#Initialisation of dictionary
dict = {}

#using json.dump()
hash = json.dumps(lst)

#creating a hash
dict[hash] = "converted"

#Printing dictionary
print(dict)
