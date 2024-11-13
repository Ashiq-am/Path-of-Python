# Python Program to create a function to get a dictionary of names.
# Here, we will start with a dictionary of three names


def function(**kwargs):
	for key, value in kwargs.items():
		print("The value of {} is {}".format(key, value))


function(name_1="Shrey", name_2="Rohan", name_3="Ayush")
