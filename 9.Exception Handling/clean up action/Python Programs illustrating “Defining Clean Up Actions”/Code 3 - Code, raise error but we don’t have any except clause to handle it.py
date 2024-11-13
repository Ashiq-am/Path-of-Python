# Python code to illustrate
# clean up actions
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
	finally:
		print("I'm finally clause, always raised !! ")

# Look at parameters and note the working of Program
divide(3, "3")



#So, clean-up action is taken first and then the error(by default) is raised by the compiler.


