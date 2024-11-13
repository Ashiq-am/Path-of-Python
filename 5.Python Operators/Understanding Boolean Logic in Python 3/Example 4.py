def check_greater(num_1, num_2):
	if num_2 > num_1:

		# after evaluating condition if it return True
		# then the following line of code get executed
		print("num_2 is greater than num_1")

	else:
		print("num_2 is not greater than num_1")

if __name__ == "__main__":
	num_1 = 3
	num_2 = 5

	# passing it to our function
	check_greater(num_1, num_2)
