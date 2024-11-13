# import library
import re

print(bool(re.match("^[A-Za-z0-9_-]*$",
					'ValidString12-_')))

print(bool(re.match("^[A-Za-z0-9_-]*$",
					'inv@lidstring')))
