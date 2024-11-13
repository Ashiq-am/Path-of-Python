global_var = 42

def modify_global():
	try:
		local_var = global_var + 1
	except Exception as e:
		print("An error occurred:", e)
	print(global_var) # Access the global variable directly
