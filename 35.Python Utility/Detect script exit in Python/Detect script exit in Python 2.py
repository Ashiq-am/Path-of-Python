import atexit

n = 2
print("Value of n:",n)

# Using register() as a decorator
@atexit.register
def goodbye():
	print("Exiting Python Script!")
