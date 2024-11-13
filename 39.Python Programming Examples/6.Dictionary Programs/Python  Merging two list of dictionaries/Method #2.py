# Python code to merge two list of dictionaries
# based on some value.

# List initialization
Input1 = [{'roll_no': ['123445', '1212'], 'school_id': 1},
		{'roll_no': ['HA-4848231'], 'school_id': 2}]
Input2 = [{'roll_no': ['473427'], 'school_id': 2},
		{'roll_no': ['092112'], 'school_id': 5}]

# Iterating and using extend to convert
for elm2 in Input2:

	for elm1 in Input1:
		if elm2['school_id'] == elm1['school_id']:
			elm1['roll_no'].extend(elm2['roll_no'])
			break
	else:
		Input1.append(elm2)

# printing
print(Input1)
