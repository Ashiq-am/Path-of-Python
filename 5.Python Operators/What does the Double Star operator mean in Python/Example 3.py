# Python Program to create a function to get a dictionary of as many names
# you want to include in your Dictionary


def function(**kwargs):
	for key, value in kwargs.items():
		print("The value of {} is {}".format(key, value))


function(
	name_1="Ayush",
	name_2="Aman",
	name_3="Harman",
	name_4="Babber",
	name_5="Striver",
)
