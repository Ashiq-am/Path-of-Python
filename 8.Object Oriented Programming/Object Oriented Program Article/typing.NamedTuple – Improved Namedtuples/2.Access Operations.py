# importing the module
from typing import NamedTuple


# creating a class
class Website(NamedTuple):
    name: str
    url: str
    rating: int


# creating a NamedTuple
website1 = Website('GeeksforGeeks',
                   'geeksforgeeks.org',
                   5)

# accessing using index
print("The name of the website is : ", end="")
print(website1[0])

# accessing using name
print("The URL of the website is : ", end="")
print(website1.url)

# accessing using getattr()
print("The rating of the website is : ", end="")
print(getattr(website1, 'rating'))
