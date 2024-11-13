def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 positional argument
student('John')

# 3 positional arguments
student('John', 'Gates', 'Seventh')

# 2 positional arguments
student('John', 'Gates')
student('John', 'Seventh')





'''In the first call, there is only one required argument and the rest arguments use the default values. 
In the second call, lastname and standard arguments value is replaced from default value to new passing value. 
We can see order of arguments is important from 2nd, 3rd, and 4th call of function.'''