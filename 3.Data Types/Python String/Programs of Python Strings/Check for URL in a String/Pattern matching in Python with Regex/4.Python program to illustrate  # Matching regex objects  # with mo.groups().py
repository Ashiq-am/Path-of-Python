# Python program to illustrate
# Matching regex objects
# with mo.groups()
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
areaCode, mainNumber = mo.groups()
print(mainNumber)
