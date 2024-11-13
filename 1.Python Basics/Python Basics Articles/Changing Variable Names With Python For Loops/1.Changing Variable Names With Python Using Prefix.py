# Adding Prefix to Variable Names
original_names = ["x", "y", "z"]
prefixed_names = []

for name in original_names:
	prefixed_name = "var_" + name
	prefixed_names.append(prefixed_name)

print("Original Names:", original_names)
print("Prefixed Names:", prefixed_names)
