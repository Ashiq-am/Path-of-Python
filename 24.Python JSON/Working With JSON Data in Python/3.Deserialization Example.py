import json

json_var =""" 
{ 
	"Country": { 
		"name": "INDIA", 
		"Languages_spoken": [ 
			{ 
				"names": ["Hindi", "English", "Bengali", "Telugu"] 
			} 
		] 
	} 
} 
"""
var = json.loads(json_var)

