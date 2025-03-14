# Python3 code to demonstrate
# swap of key and value

# initializing dictionary
old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}

# Printing original dictionary
print("Original dictionary is : ")
print(old_dict)

print()
new_dict = {}
for key, value in old_dict.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value] = [key]

    # Printing new dictionary after swapping
# keys and values
print("Dictionary after swapping is : ")
print("keys: values")
for i in new_dict:
    print(i, " :", new_dict[i])
