# Python program to illustrate
# fnmatch.fnmatch(filename, pattern)
import fnmatch
import os

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)

files = os.listdir('.')
for name in files:
	print('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern)))
