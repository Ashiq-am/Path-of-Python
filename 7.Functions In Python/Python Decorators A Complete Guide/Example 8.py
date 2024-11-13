def decorator_arguments(function):
	def wrapper_arguments(arg1, arg2):
		print("Arguments accepted are: {0}, {1}".format(arg1, arg2))
		function(arg1, arg2) # calls the function hobbies

	return wrapper_arguments

@decorator_arguments
def hobbies(hobby_one, hobby_two):
	print("My Hobbies are {0} and {1}".format(hobby_one, hobby_two))

def main():
	hobbies("Travelling", "Reading")

if __name__ == "__main__":
	main()
