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

<a class="example" href="www.geeksforgeeks.com" id="dsx_23">java</a> 
<a class="example" href="www.geeksforgeeks.com/python" id="sdcsdsdf">python</a> 
</body> 
</html> 
"""
soup = BeautifulSoup(html_doc, "lxml")

# traverse CSS from soup
print("display by CSS class:")
print(soup.select(".example"))
