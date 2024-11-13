# Positional-Only argument
def function(a, b, /, c, d, *, e, f):
	print (a, b, c, d, e, f)

function(1, 2, 3, d = 4, e = 5, f = 6) # It works fine
function(1, 2, 3, d = 4, e = 5, f = 6) # Error occurred



"""
function(1, 2, 3, d = 4, 5, f = 6) # Error occurred

"""
