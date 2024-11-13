# importing the module
import json

# opening the JSON file
data = open('file.json', )

print("Datatype before deserailization : " + str(type(data)))

# deserailizing the data
data = json.load(data)

print("Datatype after deserailization : " + str(type(data)))
