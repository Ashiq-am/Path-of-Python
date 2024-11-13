# Import required modules
import newspaper

# Define list of urls
list_of_urls = ['https://www.geeksforgeeks.org/how-to-get-the-magnitude-of-a-vector-in-numpy/',
				'https://www.geeksforgeeks.org/3d-wireframe-plotting-in-python-using-matplotlib/',
				'https://www.geeksforgeeks.org/difference-between-small-data-and-big-data/']

# Parse through each url and display its content
for url in list_of_urls:
	url_i = newspaper.Article(url="%s" % (url), language='en')
	url_i.download()
	url_i.parse()
	print(url_i.text)
