def paginate(items, page_size, page_number):
	start_index = (page_number - 1) * page_size
	end_index = start_index + page_size
	return items[start_index:end_index]

# Example usage
# Example: a list of numbers from 1 to 100
all_items = list(range(1, 101))

page_size = 10 # Number of items per page
page_number = 1 # Page number to retrieve

current_page = paginate(all_items, page_size, page_number)
print(f"Page {page_number}: {current_page}")
