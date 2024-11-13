from bs4 import BeautifulSoup
import requests

# Assign URL
url = "https://www.geeksforgeeks.org/"

# Fetch raw HTML content
html_content = requests.get(url).text

# Now that the content is ready, iterate
# through the content using BeautifulSoup:
soup = BeautifulSoup(html_content, "html.parser")

# similarly to get all the occurences of a given tag
texts = soup.find_all('p')
for text in texts:
	print(text.get_text())
