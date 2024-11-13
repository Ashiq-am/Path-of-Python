def process_data(website, topic, author, views):
	# process data here
	print("Processing data - Website:", website)
	print("Topic:", topic)
	print("Author:", author)
	print("Views:", views)

def wrapper_function(**kwargs):
	# additional processing or validation can be done here
	return process_data(**kwargs)

# data
data = {
	'website': 'GeeksforGeeks',
	'topic': 'Python',
	'author': 'Geek User 1',
	'views': 1000
}

# call the wrapper function
wrapper_function(**data)
