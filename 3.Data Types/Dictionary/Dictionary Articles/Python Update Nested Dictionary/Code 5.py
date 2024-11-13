from flatten_dict import flatten
from flatten_dict import unflatten

# an employee record
Employee = {
	'emp1': {
		'name': 'Lisa',
		'age': '29',
		'Designation':'Programmer'
			},
		'emp2': {
			'name': 'Steve',
			'age': '25',
			'Designation':'HR'
				}
			}

# flattening the dictionary, default
# reducer is 'tuple'
dict3 = flatten(Employee)

print("Flattened dictionary :", dict3)

# adding new key-value pair to second
# employee's record
dict3[('emp2', 'salary')]= 34000

print(dict3)

# unflattening the dictionary, default
# splitter is 'tuple'
Employee = unflatten(dict3)

print("\nUnflattened and updated dictionary :", Employee)
