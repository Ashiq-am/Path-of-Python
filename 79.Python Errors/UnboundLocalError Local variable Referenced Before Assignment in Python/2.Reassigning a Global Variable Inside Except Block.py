global_var = 42

def modify_global():
	try:
		global_var += 1
	except Exception as e:
		print("An error occurred:", e)
	print(global_var)

# Calling the function
modify_global()
