# Code to explain Decorators
def decorating(function):
	def item():
		print("The function was decorated.")
		function()
	return item

def my_function():
	print("This is my function.")

my_function()

decorate = decorating(my_function)
decorate()
