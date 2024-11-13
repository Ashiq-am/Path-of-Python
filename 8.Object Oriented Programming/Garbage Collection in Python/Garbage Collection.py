# Literal 9 is an object
b = 9

# Reference count of object 9
# becomes 0.
b = 4


#The literal value 9 is an object. The reference count of object 9 is incremented to 1 in line 1.
# In line 2 its reference count becomes zero as it is dereferenced.
# So garbage collector deallocates the object.




def create_cycle():

	# create a list x
	x = [ ]

	# A reference cycle is created
	# here as x contains reference to
	# to self.
	x.append(x)

create_cycle()




#A reference cycle is created when there is no way the reference count of the object can reach.
# Reference cycles involving lists, tuples, instances, classes, dictionaries, and functions are common.
# The easiest way to create a reference cycle is to create an object which refers to itself as in the example avobe:
#Because create_cycle() creates an object x which refers to itself,
# the object x will not automatically be freed when the function returns.
# This will cause the memory that x is using to be held onto until the Python garbage collector is invoked.