# import module
from bs4 import BeautifulSoup

# Html doc
html_doc = """ 
<html> 
<head> 
<title>Geeks</title> 
</head> 
<body> 
<h2>paragraphs</h2> 

<p>Welcome geeks.</p> 


<p>Hello geeks.</p> 

</body> 
</html> 
"""
soup = BeautifulSoup(html_doc, 'html.parser')

# traverse paragraphs from soup
for data in soup.find_all("p"):
	print(data.get_text())
