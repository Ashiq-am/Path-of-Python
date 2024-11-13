# Python program to illustrate
# matching a regular expression
# with plus(+)
import re
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
