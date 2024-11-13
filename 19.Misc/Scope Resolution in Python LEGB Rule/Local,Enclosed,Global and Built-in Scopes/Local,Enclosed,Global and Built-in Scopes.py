''''''


"""
The final check can be done by importing pi from math module and commenting the global, enclosed and 
local pi variables as shown below
"""





# Built-in Scope
from math import pi

# pi = 'global pi variable'

def outer():
	# pi = 'outer pi variable'
	def inner():
		# pi = 'inner pi variable'
		print(pi)
	inner()

outer()









"""
Since, pi is not defined in either local, enclosed or global scope, the built-in scope is looked 
up i.e the pi value imported from math module. Since the program is able to find the value of pi 
in the outermost scope, the following output is obtained
"""