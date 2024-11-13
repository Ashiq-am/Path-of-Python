# importing module
from bs4 import BeautifulSoup

markup = """

<!DOCTYPE>
<html>
<head><title>Example</title></head>
	<body>
		<div class="first"> Div with Class first
		</div>
		<p class="first"> Para with Class first
		</p>

		<div class="second"> Div with Class second
		</div>
		<span class="first"> Span with Class first
		</span>
	</body>
</html>
"""

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

# printing tags with given class name
for i in soup.find_all(class_="first"):
	print(i.name)
