# import module
from bs4 import BeautifulSoup

# URL for scrapping data
markup = '<a href="https://www.geeksforgeeks.org/">Welcome to <i>geeksforgeeks.com</i></a>'

# get URL html
soup = BeautifulSoup(markup, 'html.parser')

# display before decompose
print("Before Decompose")
print(soup.a)

# decomposing the
# soup data
new_tag = soup.a.decompose()
print("After decomposing:")
print(new_tag)
