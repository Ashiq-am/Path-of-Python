# Python program to illustrate
# matching a regular expression
# with plus(+)
import re
batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batman')== None
print(mo3)
