import re


''' 
Meta characters - 
* - 0 or more 
+ - 1 or more 
? - 0 or 1 
{m} - m times 
{m,n} - min m and max n 
'''

test_phrase = 'sddsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = [r'sd*',	 # s followed by zero or more d's
				r'sd+',		 # s followed by one or more d's
				r'sd?',		 # s followed by zero or one d's
				r'sd{3}',	 # s followed by three d's
				r'sd{2,3}',	 # s followed by two to three d's
				]


def multi_re_find(test_patterns, test_phrase):
	for pattern in test_patterns:
		compiledPattern = re.compile(pattern)
		print('finding {} in test_phrase'.format(pattern))
		print(re.findall(compiledPattern, test_phrase))


multi_re_find(test_patterns, test_phrase)
