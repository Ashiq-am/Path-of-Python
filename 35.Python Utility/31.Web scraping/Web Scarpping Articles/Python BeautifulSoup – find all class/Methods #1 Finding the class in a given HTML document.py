# html code
html_doc = """<html><head><title>Welcome to geeksforgeeks</title></head> 
<body> 
<p class="title"><b>Geeks</b></p> 


<p class="body">geeksforgeeks a computer science portal for geeks 
</body> 
"""

# import module
from bs4 import BeautifulSoup

# parse html content
soup = BeautifulSoup( html_doc , 'html.parser')

# Finding by class name
soup.find( class_ = "body" )
