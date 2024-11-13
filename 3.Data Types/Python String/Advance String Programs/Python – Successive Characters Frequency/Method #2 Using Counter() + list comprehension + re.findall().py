# Python3 code to demonstrate working of
# Successive Characters Frequency
# Using Counter() + list comprehension + re.findall()
from collections import Counter
import re

# initializing string
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'

# printing original string
print("The original string is : " + str(test_str))

# initializing word
que_word = "geek"

# Successive Characters Frequency
# Using Counter() + list comprehension + re.findall()
res = dict(Counter(re.findall(f'{que_word}(.)', test_str,
									flags=re.IGNORECASE)))

# printing result
print("The Characters Frequency is : " + str(res))
