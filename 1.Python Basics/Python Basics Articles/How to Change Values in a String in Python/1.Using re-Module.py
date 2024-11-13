import re

def rename_variables(code, old_name, new_name):
	return re.sub(rf"\b{old_name}\b", new_name, code)

old_code = "x = 5; y = x + 3;"
new_code = rename_variables(old_code, "x", "z")
print(new_code)
