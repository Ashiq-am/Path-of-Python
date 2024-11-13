def rename_variables(code, old_name, new_name):
	return code.replace(old_name, new_name)

old_code = "x = 5; y = x + 3;"
new_code = rename_variables(old_code, "x", "geeksforgeeks")
print(new_code)
