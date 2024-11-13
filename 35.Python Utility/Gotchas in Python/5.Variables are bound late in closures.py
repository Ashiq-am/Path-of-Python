def create_multipliers():

	# lambda function creates an iterable
	# list anonymously
	return [lambda c : i * c for i in range(6)]


for multiplier in create_multipliers():
	print(multiplier(3))
