from bs4 import BeautifulSoup

# Read HTML content from a file
with open('ex.html', 'r', encoding='utf-8') as file:
    html_cont = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser')

# Extract text using CSS selectors
texts = soup.select('div.content > p')  # Select all <p> tags inside <div class='content'>
for text in texts:
    print(text.get_text())
