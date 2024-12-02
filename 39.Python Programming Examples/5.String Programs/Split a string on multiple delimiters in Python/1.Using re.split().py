import re

s = "apple, banana; orange grape"

# Split using re.split
res = re.split(r'[;,\s]+', s)
print(res)