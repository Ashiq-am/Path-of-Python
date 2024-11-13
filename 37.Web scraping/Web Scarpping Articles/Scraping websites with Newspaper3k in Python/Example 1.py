# Import required module
import newspaper

# Assingn url
url = 'https://www.geeksforgeeks.org/top-5-open-source-online-machine-learning-environments/'

# Extract web data
url_i = newspaper.Article(url="%s" % (url), language='en')
url_i.download()
url_i.parse()

# Display scrapped data
print(url_i.text)
