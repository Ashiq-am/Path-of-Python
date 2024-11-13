# Python code to demonstrate
# to split strings
# on uppercase letter

import re

# Initialising string
ini_str = 'GeeksForGeeks'

# Printing Initial string
print ("Initial String", ini_str)

# Splitting on UpperCase using re
res_list = []
res_list = re.findall('[A-Z][^A-Z]*', ini_str)

# Printing result
print("Resultant prefix", str(res_list))
