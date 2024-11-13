# Python3 code to demonstrate working of
# Case insensitive Replace
# Using sub() + lambda + escape()
import re

# initializing string
test_str = "gfg is BeSt"

# printing original string
print("The original string is : " + str(test_str))

# initializing replace string
repl = "good"

# initializing substring to be replaced
subs = "best"

# regex used for ignoring cases
res = re.sub('(?i)' + re.escape(subs), lambda m: repl, test_str)

# printing result
print("Replaced String : " + str(res))
