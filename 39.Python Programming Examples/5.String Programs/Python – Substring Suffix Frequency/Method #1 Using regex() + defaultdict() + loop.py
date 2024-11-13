# Python3 code to demonstrate working of
# Substring substitutes frequency
# Using regex() + defaultdict() + loop
from collections import defaultdict
import re

# initializing string
test_str = "Gfg is good . Gfg is best . Gfg is better . Gfg is good ."

# printing original string
print("The original string is : " + str(test_str))

# initializing substring
substr = "Gfg is"

# initializing regex
temp = re.findall(substr + " (\w+)", test_str, flags = re.IGNORECASE)

# adding values to form frequencies
res = defaultdict(int)
for idx in temp:
    res[idx] += 1

# printing result
print("Frequency of replacements : " + str(dict(res)))
