# Dictionary with student data
data = {'Student No': {1, 2, 3, 4, 5},
		'Student Aadhar No': {11, 22, 33, 44, 55}}

# using setdefault() method to get aadhar number
# of the students
print(data.setdefault('Student Aadhar No'))

# using setdefault() method to get aadhar number
# of the students
print(data.setdefault('Student No'))

# set the third set using setdefault method for
# student names
data = data.setdefault(
	'Student Names', {'sravan', 'gopi', 'ramya','durga', 'sudheer'})

# display
data
