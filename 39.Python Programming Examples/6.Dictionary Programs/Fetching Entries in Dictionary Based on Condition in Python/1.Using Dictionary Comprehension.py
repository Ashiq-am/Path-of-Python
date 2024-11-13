# initializing dictionary
original_dict = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 68}

filtered_dict = {key: value for key,
				value in original_dict.items() if value >= 75}

# Displaying the result
print("Dictionary Comprehension:", filtered_dict)
