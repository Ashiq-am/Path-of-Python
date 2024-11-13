# Python code to demonstrate
# to find nth occurrence of substring

import re

# Initialising values
ini_str = "abababababab"
substr = "ab"
occurrence = 4

# Finding nth occurrence of substring
inilist = [m.start() for m in re.finditer(r"ab", ini_str)]
if len(inilist) >= 4:

    # Printing result
    print("Nth occurrence of substring at", inilist[occurrence - 1])
else:
    print("No {} occurrence of substring lies in given string".format(occurrence))
