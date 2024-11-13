def process_data(website, topic, author, views):
	# process data here
	print("Processing data - Website:", website)
	print("Topic:", topic)
	print("Author:", author)
	print("Views:", views)

def main_function(website, topic, author, views):
	# pass the parameters explicitly to another function
	process_data(website=website, topic=topic, author=author, views=views)

# data
data = {
	'website': 'GeeksforGeeks',
	'topic': 'Python',
	'author': 'Geek User 1',
	'views': 1000
}

# call the main function with explicit parameter passing
main_function(**data)
