# Python program to illustrate
# matching a regular expression
# with plus(+)
import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
