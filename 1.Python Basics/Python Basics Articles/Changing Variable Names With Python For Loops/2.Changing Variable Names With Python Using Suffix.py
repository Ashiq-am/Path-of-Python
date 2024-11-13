# Adding Suffix to Variable Names
original_names = ["x", "y", "z"]
suffixed_names = []

for name in original_names:
	suffixed_name = name + "_new"
	suffixed_names.append(suffixed_name)

print("Original Names:", original_names)
print("Suffixed Names:", suffixed_names)
