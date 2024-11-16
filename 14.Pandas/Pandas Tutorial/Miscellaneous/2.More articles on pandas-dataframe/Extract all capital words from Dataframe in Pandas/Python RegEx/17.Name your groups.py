import re


match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})',
				'26-08-2020')
print(match.group('mm'))
