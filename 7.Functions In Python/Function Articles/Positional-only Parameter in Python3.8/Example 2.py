# Positional-Only argument
def function(a, b, /, **kwargs):
	print (a, b, kwargs)

function(1, 2, a = 4, b = 5, c = 6) # It works fine
function(1, 2, a = 4, b = 5, c = 6) # Error occurred



"""
function(a = 1, 2, a = 4, b = 5, c = 6) # Error occurred

"""
