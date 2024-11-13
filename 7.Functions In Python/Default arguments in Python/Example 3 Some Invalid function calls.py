def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# required argument missing
student()

# non keyword argument after a keyword argument
student(firstname ='John', 'Seventh')

# unknown keyword argument
student(subject ='Maths')








'''Above code will throw error because –

In the first call, value is not passed for parameter firstname which is the required parameter.
In the second call, there is non-keyword argument after a keyword argument.
In the third call, the passing keyword argument is not matched with the actual keyword name arguments.'''
