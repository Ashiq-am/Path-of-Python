import json

data = {
	"name": "Satyam kumar",
	"place": "patna",
	"skills": [
		"Raspberry pi",
		"Machine Learning",
		"Web Development"
	],
	"email": "xyz@gmail.com",
	"projects": [
		"Python Data Mining",
		"Python Data Science"
	]
}
with open( "data_file.json" , "w" ) as write:
	json.dump( data , write )
