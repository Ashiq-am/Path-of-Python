# initializing dictionary
original_dict = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 68}

filtered_dict = {}
for key, value in original_dict.items():
	if value >= 75:
		filtered_dict[key] = value

# Displaying the result
print("Items() Method with Loop:", filtered_dict)
