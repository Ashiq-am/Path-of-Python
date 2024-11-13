ht_doc = """
<html><head><title>Geeks For Geeks</title></head>
<body>
<p class="title"><b>most viewed courses in GFG,its all free</b></p>

<p class ="prog">Top 5 Popular Programming Languages</p>

<a href="https://www.geeksforgeeks.org/java-programming-examples/"\
class="prog" id="link1">Java</a>
<a href="https://www.geeksforgeeks.org/cc-programs/" class="prog" \
id="link2">c/c++</a>
<a href="https://www.geeksforgeeks.org/python-programming-examples/"\
class="prog" id="link3">Python</a>
<a href="https://https://www.geeksforgeeks.org/introduction-to-javascript/"\
class="prog" id="link4">Javascript</a>
<a href="https://www.geeksforgeeks.org/ruby-programming-language/"\
class="prog" id="link5">Ruby</a>
according to an online survey. </a>
<p class="prog"> Programming Languages</p>

</body></html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(ht_doc, 'html.parser')

# embedding html document
Itag = soup.title

# assigning title tag of BeautifulSoup-assigned variable
# to print parent element in Itag variable
print(Itag.parent)
htmlTag = soup.html
print(type(htmlTag.parent))
print(soup.parent)
