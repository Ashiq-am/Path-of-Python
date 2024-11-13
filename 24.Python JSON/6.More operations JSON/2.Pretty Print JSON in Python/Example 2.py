import json

# Opening JSON file
f = open('myfile.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

print(json.dumps(data, indent=1))

# Closing file
f.close()
