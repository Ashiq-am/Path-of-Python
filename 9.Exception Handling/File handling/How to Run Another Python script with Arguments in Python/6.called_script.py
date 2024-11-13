def main(arg1, arg2, arg3):
	# Print arguments
	print(f"Arguments received: {arg1}, {arg2}, {arg3}")


if __name__ == "__main__":
	import sys
	# Retrieve arguments
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	arg3 = sys.argv[3]
	# Call main function
	main(arg1, arg2, arg3)
