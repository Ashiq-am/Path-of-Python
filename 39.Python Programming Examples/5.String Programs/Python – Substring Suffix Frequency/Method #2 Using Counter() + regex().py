# Python3 code to demonstrate working of
# Substring substitutes frequency
# Using Counter() + regex()
import re
from collections import Counter

# initializing string
test_str = "Gfg is good . Gfg is best . Gfg is better . Gfg is good ."

# printing original string
print("The original string is : " + str(test_str))

# initializing substring
substr = "Gfg is"

# initializing regex
temp = re.findall(substr + " (\w+)", test_str, flags = re.IGNORECASE)

# adding values to form frequencies
res = dict(Counter(temp))

# printing result
print("Frequency of replacements : " + str(res))
