# Python program to illustrate
# fnmatch.translate(pattern)
import fnmatch, re

regex = fnmatch.translate('*.txt')
reobj = re.compile(regex)

print(regex)
print(reobj.match('foobar.txt'))
