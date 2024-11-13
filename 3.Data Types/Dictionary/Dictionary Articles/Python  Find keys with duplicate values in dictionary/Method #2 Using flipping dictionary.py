# Python code to demonstrate
# finding duplicate values from dictionary

# initialising dictionary
ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}

# printing initial_dictionary
print("initial_dictionary", str(ini_dict))

# finding duplicate values
# from dictionary using flip
flipped = {}

for key, value in ini_dict.items():
	if value not in flipped:
		flipped[value] = [key]
	else:
		flipped[value].append(key)

# printing result
print("final_dictionary", str(flipped))
