def modify_variable(var):
	var += 10
	return var

# Define a variable outside the function
original_var = 5

# Passing the variable to the function
modified_var = modify_variable(original_var)
print(modified_var)
