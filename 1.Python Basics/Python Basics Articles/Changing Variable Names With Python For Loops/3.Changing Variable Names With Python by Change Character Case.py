# Changing Case of Variable Names
original_names = ["varOne", "VarTwo", "VarThree"]
lowercase_names = []

for name in original_names:
	lowercase_name = name.lower()
	lowercase_names.append(lowercase_name)

print("Original Names:", original_names)
print("Lowercase Names:", lowercase_names)
