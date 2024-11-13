''''''


"""
Local scope refers to variables defined in current function.Always, a function will first look up for 
a variable name in its local scope. Only if it does not find it there, the outer scopes are checked.
"""




# Local Scope

pi = 'global pi variable'
def inner():
	pi = 'inner pi variable'
	print(pi)

inner()










'''On running the above program, the execution of the inner function prints the value of its local
(highest priority in LEGB rule) variable pi because it is defined and available in the local scope'''