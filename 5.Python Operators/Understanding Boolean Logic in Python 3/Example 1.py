def check_Empty(list_name):
	print(bool(list_name))

if __name__ == "__main__":
	# making an empty list
	my_list =[]

	# calling our function
	check_Empty(my_list)

	# making an non-empty list
	my_list1 =[1, 2, 3]

	# calling our function
	check_Empty(my_list1)
