# Python code to demonstrate
# to split strings
# on uppercase letter

import re

# Initialising string
ini_str = 'GeeksForGeeks'

# Printing Initial string
print ("Initial String", ini_str)

# Splitting on UpperCase using re
res_list = [s for s in re.split("([A-Z][^A-Z]*)", ini_str) if s]

# Printing result
print("Resultant prefix", str(res_list))
