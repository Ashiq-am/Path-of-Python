def decorator_arguments(function):

	def wrapper_arguments(arg1, arg2):
		print(" Arguments accepted are: {0}, {1}".format(arg1, arg2))

	return wrapper_arguments

@decorator_arguments
def hobbies(hobby_one, hobby_two):
	print("My Hobbies are {0} and {1}".format(hobby_one, hobby_two))

def main():

	# the reference of wrapper_arguments
	# is returned
	hob = hobbies
	print(hob)

	# passing the arguments to the
	# wrapper_arguments
	hob('Travelling', 'Reading')

main()
