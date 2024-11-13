# Python program to illustrate the use of
# Accessor and Mutator methods

# Defining class Car
class Car:

	# Defining method init method with a parameter
	def __init__(self, carname):
		self.__make = carname

	# Defining Mutator Method
	def set_make(self, carname):
		self.__make = carname

	# Defining Accessor Method
	def get_make(self):
		return self.__make

# Creating an object
myCar = Car('Ford');

# Accesses the value of the variable
# using Accessor method and then
# prints it
print (myCar.get_make())

# Modifying the value of the variable
# using Mutator method
myCar.set_make('Porche')

# Prints the modified value
print (myCar.get_make())
