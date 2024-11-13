#import html
import html

try:
	# Python 2.6-2.7
	from HTMLParser import HTMLParser
except ImportError:
	# Python 3
	from html.parser import HTMLParser

# for python 3
h = html.parser
print(h.unescape('Γeeks for Γeeks'))
