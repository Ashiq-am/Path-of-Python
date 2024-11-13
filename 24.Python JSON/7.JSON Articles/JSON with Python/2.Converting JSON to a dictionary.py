# Python program to convert JSON to Dict


import json

# JSON string
employee ='{"name": "Nitin", "department":"Finance",\
"company":"GFG"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print("Data after conversion")
print(employee_dict)
print(employee_dict['department'])

print("\nType of data")
print(type(employee_dict))
