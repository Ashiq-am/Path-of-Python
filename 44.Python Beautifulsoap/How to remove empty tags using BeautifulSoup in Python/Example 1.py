# Import Module
from bs4 import BeautifulSoup

# HTML Object
html_object = """

<p>
<p></p>
<strong>some<br>text<br>here</strong></p>

"""

# Get HTML Code
soup = BeautifulSoup(html_object, "lxml")

# Iterate each line
for x in soup.find_all():

    # fetching text from tag and remove whitespaces
    if len(x.get_text(strip=True)) == 0:
        # Remove empty tag
        x.extract()

# Print HTML Code with removed empty tags
print(soup)
