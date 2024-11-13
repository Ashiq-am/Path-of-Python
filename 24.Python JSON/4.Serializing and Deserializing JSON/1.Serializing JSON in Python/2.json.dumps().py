# import module
import json

# Data to be written
data = {
	"user": {
		"name": "satyam kumar",
		"age": 21,
		"Place": "Patna",
		"Blood group": "O+"
	}
}

# Serializing json
res = json.dumps( data )
print( res )
