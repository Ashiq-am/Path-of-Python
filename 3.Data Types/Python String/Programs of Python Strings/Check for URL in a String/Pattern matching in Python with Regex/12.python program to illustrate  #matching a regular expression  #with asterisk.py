#python program to illustrate
#matching a regular expression
#with asterisk(*)
import re
batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
