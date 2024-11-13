def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# required argument missing
student()

# non keyword argument after a keyword argument
student(firstname ='John')

# unknown keyword argument
student(subject ='Maths')
