# import module
from goose3 import Goose

# var for URL
url = "https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar"

# initialization with
article = Goose().extract(url)
