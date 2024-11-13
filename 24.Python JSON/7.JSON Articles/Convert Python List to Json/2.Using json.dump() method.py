import json
from google.colab import files

# List of lists
data = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

# Convert into JSON
# File name is mydata.json
with open("mydata.json", "w") as final:
	json.dump(data, final)

# Download the file
files.download('mydata.json')
