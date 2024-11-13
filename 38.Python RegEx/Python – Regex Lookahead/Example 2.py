# importing regex
import re

# Lookahead example
example = re.search(r'geeks(?=[a-z])',
					"geeks123")

# output
print(example)
