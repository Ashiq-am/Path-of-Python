# Python program to write JSON
# to a file


import json

# Data to be written
dictionary ={
	"name" : "Nisha",
	"rollno" : 420,
	"cgpa" : 10.10,
	"phonenumber" : "1234567890"
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)
