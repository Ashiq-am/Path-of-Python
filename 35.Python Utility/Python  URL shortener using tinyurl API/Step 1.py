from __future__ import with_statement

import contextlib

try:
	from urllib.parse import urlencode

except ImportError:
	from urllib import urlencode

try:
	from urllib.request import urlopen

except ImportError:
	from urllib2 import urlopen

import sys
