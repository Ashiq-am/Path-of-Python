# importing module
from bs4 import BeautifulSoup

markup = """
<html>
	<head>
		<title>GEEKS FOR GEEKS EXAMPLE</title>
	</head>
	<body>
		<p class="1"><b>Geeks for Geeks</b></p>

		<p class="coding">A Computer Science portal for geeks.
			<h1>Heading</h1>
			<b class="gfg">Programming Articles</b>,
			<b class="gfg">Programming Languages</b>,
			<b class="gfg">Quizzes</b>;
		</p>

		<p class="coding">practice</p>

	</body>
</html>
	"""

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

parent = soup.find(class_="coding")

# assign n
n = 2

# print the 2nd <b> of parent
print(parent.select("b:nth-of-type("+str(n)+")"))
print()

# print the <b> which is the 2nd child of the parent
print(parent.select("b:nth-child("+str(n)+")"))
