# Python program to illustrate
# matching a regular expression
# with asterisk(*)
import re
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
