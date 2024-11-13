import json

# create a list to store extracted json objects
extracted_objs = []
# open the file in read mode

with open('data.json', 'r') as file:
    # Iterate over each line
    for line in file:
        # Parse the JSON object from the current line
        json_obj = json.loads(line)
        extracted_objs.append(json_obj)

# print all extracted JSON Objects
print(extracted_objs)
