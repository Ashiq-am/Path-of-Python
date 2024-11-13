# importing module
from bs4 import BeautifulSoup
import requests

# assign website
sample_website='https://www.geeksforgeeks.org/python-programming-language/'
page=requests.get(sample_website)

# parsering string to HTML
soup = BeautifulSoup(page.content, 'html.parser')
parent = soup.find(class_="wrapper")

# assign n
n = 1

# print the 2nd <b> of parent
print(parent.select("b:nth-of-type("+str(n)+")"))
print()

# print the <b> which is the 2nd child of the parent
print(parent.select("b:nth-child("+str(n)+")"))
