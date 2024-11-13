def func():

	# defining variable
	a_variable = 0

	# using globals() function check
	# if global variable exist
	is_global_var = "a_variable" in globals()

	# printing result
	print(is_global_var)

# driver code
func()
