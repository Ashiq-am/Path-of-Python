import re


match = re.search(r'(?P<first_two>[\d]{2})-(?P<last_three>[\d]{3})',\
				'25-542', re.DEBUG)
print(match)
