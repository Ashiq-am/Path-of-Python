# Extract nested data using recursion
def extract_data_recursive(data, keys):
	return data[keys[0]] if len(keys) == 1 else extract_data_recursive(data[keys[0]], keys[1:])


edu_department_recursive = extract_data_recursive(
	data, ["organizations", 0, "departments", 0])

print(f"Extracted Data using Recursion:")
print(f"Educational Department (Recursive): {edu_department_recursive}")
