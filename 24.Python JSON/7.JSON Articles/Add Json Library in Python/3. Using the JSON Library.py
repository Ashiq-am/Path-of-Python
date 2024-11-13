# create a dictionary
data = {"name": "GFG", "age": 1, "skills": [
	"writing", "coding", "answering questions"]}

# convert the dict in to the json string
json_string = json.dumps(data)

# print the json string
print(json_string)

# json string to python conversion
new_data = json.loads(json_string)

print(new_data["name"])
