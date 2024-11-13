# declare fun1
def fun1():

	# create a local variable for fun1
	var = "local"

	# declare fun2
	def fun2():

		# declare nonlocal function
		nonlocal var

		# assign value in nonlocal variable
		var = "nonlocal"

		# print inner var
		print("inner:", var)

	# call fun2
	fun2()

	# print outer var
	print("outer:", var)

# call fun1 for executing the program
fun1()
