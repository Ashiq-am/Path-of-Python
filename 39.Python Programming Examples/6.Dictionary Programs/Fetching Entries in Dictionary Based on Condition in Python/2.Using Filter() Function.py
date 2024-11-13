original_dict = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 68}

# Define a filtering function
def filter_scores(item):
	return item[1] >= 75

filtered_dict = dict(filter(filter_scores, original_dict.items()))

# Displaying the result
print("Filter() Function:", filtered_dict)
