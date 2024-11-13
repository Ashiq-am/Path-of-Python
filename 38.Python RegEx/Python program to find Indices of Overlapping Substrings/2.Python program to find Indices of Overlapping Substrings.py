# Import required module
import re


# Explicit function to Count
# Indices of Overlapping Substrings
def CntSubstr(pattern, string):
	a = [m.start() for m in re.finditer(
		'(?={0})'.format(re.escape(pattern)), string)]
	return a


# Driver Code
string1 = 'geeksforgeeksforgeeks'
pattern1 = 'geeksforgeeks'

string2 = 'barfoobarfoobarfoobarfoobarfoo'
pattern2 = 'foobarfoo'


# Calling the function
print(CntSubstr(pattern1, string1))
print(CntSubstr(pattern2, string2))
