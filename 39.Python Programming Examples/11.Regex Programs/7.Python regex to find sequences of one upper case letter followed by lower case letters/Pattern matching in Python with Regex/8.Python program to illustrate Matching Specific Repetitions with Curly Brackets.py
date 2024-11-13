# Python program to illustrate
# Matching Specific Repetitions
# with Curly Brackets
import re
haRegex = re.compile(r'(Ha){3}')
mo2 = haRegex.search('Ha')== None
print(mo2)
