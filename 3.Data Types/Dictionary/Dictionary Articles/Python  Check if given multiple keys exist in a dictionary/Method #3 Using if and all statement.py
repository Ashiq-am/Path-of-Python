# Python3 code check multiple key existence
# using if and all

# initializing a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}

# using if, all statement
if all(key in sports for key in ('geeksforgeeks', 'practice')):
	print("keys are present")
else:
	print("keys are not present")

# using if, all statement
if all(key in sports for key in ('geeksforgeeks', 'ide')):
	print("keys are present")
else:
	print("keys are not present")
