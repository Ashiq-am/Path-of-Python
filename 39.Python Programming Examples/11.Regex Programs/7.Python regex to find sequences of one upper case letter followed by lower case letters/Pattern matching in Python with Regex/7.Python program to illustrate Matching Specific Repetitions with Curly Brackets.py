# Python program to illustrate
# Matching Specific Repetitions
# with Curly Brackets
import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
