# Python program to illustrate destructor

class Employee:

	# Initializing
	def __init__(self):
		print('Employee created')

	# Calling destructor
	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')





#This example gives the explanation of above mentioned note.
# Here, notice that the destructor is called after the ‘Program End…’ printed.