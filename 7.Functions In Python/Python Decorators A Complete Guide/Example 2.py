def reverse_decorator(function):

	def reverse_wrapper():
		make_reverse = "".join(reversed(function()))
		return make_reverse

	return reverse_wrapper

@reverse_decorator
def say_hi():
	return 'Hi George'

def main():
	print(say_hi())

if __name__ == "__main__":
	main()
