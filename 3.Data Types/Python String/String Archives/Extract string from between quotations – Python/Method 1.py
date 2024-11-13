import re
inputstring = ' some strings are present in between "geeks" "for" "geeks" '

print(re.findall('"([^"]*)"', inputstring))
