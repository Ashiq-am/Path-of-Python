# import required module
import re

# positive lookahead
example1 = re.search('geeks(?=[a-z])',
					'geeksforgeeks')
print('Positive Lookahead:', example1.group())

# negative lookahead
example2 = re.search('geeks(?![a-z])',
					'geeks123')
print('Negative Lookahead:', example2.group())
