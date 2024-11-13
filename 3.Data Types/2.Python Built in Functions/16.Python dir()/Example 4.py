# Python3 program to demonstrate working
# of dir(), when user defined objects are
# passed are parameters.


# Creation of a simple class with __dir()__
# method to demonstrate it's working
class Supermarket:

	# Function __dir()___ which list all
	# the base attributes to be used.
	def __dir__(self):
		return['customer_name', 'product',
			'quantity', 'price', 'date']


# user-defined object of class supermarket
my_cart = Supermarket()

# listing out the dir() method
print(dir(my_cart))
