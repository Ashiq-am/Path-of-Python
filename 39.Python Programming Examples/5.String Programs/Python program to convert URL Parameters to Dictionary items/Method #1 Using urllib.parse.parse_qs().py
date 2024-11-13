# import module
import urllib.parse

# initializing string
test_str = 'gfg=4&is=5&best=yes'

# printing original string
print("The original string is : " + str(test_str))

# parse_qs gets the Dictionary and value list
res = urllib.parse.parse_qs(test_str)

# printing result
print("The parsed URL Params : " + str(res))
