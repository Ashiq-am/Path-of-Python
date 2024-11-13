# Replacing Specific Characters in Variable Names
original_names = ["abc_123", "def_456", "ghi_789"]
replaced_names = []

for name in original_names:
	replaced_name = name.replace("_", "-")
	replaced_names.append(replaced_name)

print("Original Names:", original_names)
print("Replaced Names:", replaced_names)
