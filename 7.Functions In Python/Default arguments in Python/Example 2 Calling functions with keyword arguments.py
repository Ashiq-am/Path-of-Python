def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 keyword argument
student(firstname ='John')

# 2 keyword arguments
student(firstname ='John', standard ='Seventh')

# 2 keyword arguments
student(lastname ='Gates', firstname ='John')







'''In the first call, there is only one required keyword argument. 
In the second call, one is required argument and one is optional(standard), 
whose value get replaced from default to new passing value. 

In the third call, we can see that order in keyword argument is not important.'''