import re

# getting the match of the the string
search_pattern = re.search('\d+',
						'abcd')
""" 
d: stands for integer 
+: means a consecutive set of characters 
satisfying a condition. 
Hence d+ will match consecutive 
integer string 
"""

print(search_pattern.start())

print(search_pattern.end())
