# import required module
import re

# using lookahead
example1 = re.search(r'geeks(?=[a-z])',
					"geeksforgeeks")

print('Using lookahead:', example1.group())

# without using lookahead
example2 = re.search(r'geeks([a-z])',
					"geeksforgeeks")

print('Without using lookahead:', example2.group())
