def process_data(**kwargs):
	# Process data here
	print("Processing data:", kwargs)

def main_function(**kwargs):
	# Pass the **kwargs parameter to another function
	process_data(**kwargs)

# Data
data = {
	'website': 'GeeksforGeeks',
	'topic': 'Python',
	'author': 'Geek User 1',
	'views': 1000
}

# Call the main function with **kwargs
main_function(**data)
