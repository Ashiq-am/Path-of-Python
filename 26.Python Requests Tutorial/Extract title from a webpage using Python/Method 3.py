# importing the module
from mechanize import Browser

# target url
url = 'https://www.geeksforgeeks.org/'

# creating a Browser instance
br = Browser()
br.open(url)

# displaying the title
print("Title of the website is : ")
print( br.title())
