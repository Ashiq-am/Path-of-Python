import re


match = re.search(r"""(?P<first_two>[\d]{2}) # The first two digits 
		-						 # A literal python 
		(?P<last_three>[\d]{3})	 # The last three digit 
		""", '25-542', re.VERBOSE)
print(match)
