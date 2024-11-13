# Python code to demonstrate
# checking whether string
# is valid json or not

import json

ini_string = "{'akshat' : 1, 'nikhil' : 2}"

# printing initial ini_string
print ("initial string", ini_string)

# checking for string
try:
	json_object = json.loads(ini_string)
	print ("Is valid json? true")
except ValueError as e:
	print ("Is valid json? false")
