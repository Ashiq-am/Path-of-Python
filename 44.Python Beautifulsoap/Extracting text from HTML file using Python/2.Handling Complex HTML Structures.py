from bs4 import BeautifulSoup

# Read HTML content from a file
with open('example.html', 'r', encoding='utf-8') as file:
    html_cont = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser')

# Extract text from nested tags
divs = soup.find_all('div', class_='content')  # Find all <div> tags with class 'content'
for div in divs:
    paragraphs = div.find_all('p')  # Find all <p> tags within each <div class='content'>
    for p in paragraphs:
        print(p.get_text())
