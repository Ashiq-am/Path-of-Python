import json

with open('exam.json', 'r') as json_File:
	sample_load_file = json.load(json_File)

# getting hold of all values inside
# the dictionary
test = sample_load_file['criteria']

# getting hold of the values of
# variableParam
test1 = test[1].values()
test2 = list(test1)[0]
test3 = test2[1:-1].split(",")
print(test3[1])
