# Python program to illustrate
# fnmatch.fnmatchcase(filename, pattern)
import fnmatch
import os

pattern = 'FNMATCH_*.PY'
print('Pattern :', pattern)


files = os.listdir('.')

for name in files:
	print('Filename: %-25s %s' % (name, fnmatch.fnmatchcase(name, pattern)))
