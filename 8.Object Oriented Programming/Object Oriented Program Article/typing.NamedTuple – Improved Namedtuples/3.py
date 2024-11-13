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

# changing the attribute value
website1.name = "Google"
