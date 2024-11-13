# importing module
from bs4 import BeautifulSoup

markup = markup = """

<!DOCTYPE>
<html>
<head><title>Example</title></head>
	<body>

<p>
		Nested div
	</p>

		<div id="first"> Div with ID first
		<div id="second"> Div with id second
		</div>
		</div>
	</body>
</html>
"""

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

# finding the div with the id
div_bs4 = soup.find('div', id="second")

print(div_bs4.string)
