"""

"""



"""If a variable is not defined in local scope, then, it is checked for in the higher scope, 
in this case, the global scope."""






# Global Scope

pi = 'global pi variable'
def inner():
	pi = 'inner pi variable'
	print(pi)

inner()
print(pi)










'''
Therefore, as expected the program prints out the value in the local scope on execution of inner(). 
It is because it is defined inside the function and that is the first place where the variable is 
looked up. The pi value in global scope is printed on execution of print(pi) on line 9.
'''